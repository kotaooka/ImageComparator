try:
    import cv2
    import matplotlib.pyplot as plt
    import numpy as np
    import tkinter as tk
    from tkinter import filedialog, messagebox
except ImportError as e:
    print(f"エラー: 必要なライブラリがインストールされていません: {e.name}")
    print("以下のコマンドでインストールできます：")
    print(f"pip install {e.name}")
    exit()


import cv2
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import filedialog, messagebox

def select_and_display_image_A():
    file_path_A = filedialog.askopenfilename(title="画像1を選択してください", initialdir="C:/", filetypes=[("Image Files", "*.png *.jpg *.tif")])
    entryA.delete(0, tk.END)
    entryA.insert(tk.END, file_path_A)

def select_and_display_image_B():
    file_path_B = filedialog.askopenfilename(title="画像2を選択してください", initialdir="C:/", filetypes=[("Image Files", "*.png *.jpg *.tif")])
    entryB.delete(0, tk.END)
    entryB.insert(tk.END, file_path_B)

def display_image():
    file_path_A = entryA.get().encode('utf-8')
    file_path_B = entryB.get().encode('utf-8')

    if not file_path_A or not file_path_B:
        messagebox.showerror("ImageComparator - エラー", "画像が選択されていません。")
        return

    imgA = cv2.imdecode(np.fromfile(file_path_A, dtype=np.uint8), cv2.IMREAD_UNCHANGED)
    imgB = cv2.imdecode(np.fromfile(file_path_B, dtype=np.uint8), cv2.IMREAD_UNCHANGED)

    imgA = cv2.cvtColor(imgA, cv2.COLOR_BGR2RGB)
    imgB = cv2.cvtColor(imgB, cv2.COLOR_BGR2RGB)

    hA, wA, cA = imgA.shape[:3]
    hB, wB, cB = imgB.shape[:3]

    akaze = cv2.AKAZE_create()
    kpA, desA = akaze.detectAndCompute(imgA, None)
    kpB, desB = akaze.detectAndCompute(imgB, None)

    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = bf.match(desA, desB)
    matches = sorted(matches, key=lambda x: x.distance)
    good = matches[:int(len(matches) * match_ratio.get())]  

    src_pts = np.float32([kpA[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
    dst_pts = np.float32([kpB[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)
    M, mask = cv2.findHomography(dst_pts, src_pts, cv2.RANSAC, 5.0) 

    imgB_transform = cv2.warpPerspective(imgB, M, (wA, hA))

    result = cv2.absdiff(imgA, imgB_transform)
    result_gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)

    _, result_bin = cv2.threshold(result_gray, threshold.get(), 255, cv2.THRESH_BINARY)

    kernel = np.ones((2, 2), np.uint8)
    result_bin = cv2.morphologyEx(result_bin, cv2.MORPH_OPEN, kernel) 

    result_bin_rgb = cv2.cvtColor(result_bin, cv2.COLOR_GRAY2RGB)
    
    result_add = cv2.addWeighted(imgA, 0.3, result_bin_rgb, 0.7, 2.4) 

    if draw_rectangle.get():
        contours, _ = cv2.findContours(result_bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for cnt in contours:
            if cv2.contourArea(cnt) > rectangle_threshold.get():
                x, y, w, h = cv2.boundingRect(cnt)
                cv2.rectangle(result_add, (x, y), (x + w, y + h), (0, 255, 0), 2)

    plt.imshow(result_add)
    plt.title("Result Image")
    plt.axis('off')
    plt.subplots_adjust(left=0.05, right=0.995, bottom=0.05, top=0.90)
    plt.show()


def click_close():
    if messagebox.askokcancel("ImageComparator - 確認", "終了しますか？"):
        main.destroy()


main = tk.Tk()
main.title("ImageComparator")
main.geometry("700x450")  # ウィンドウのサイズを設定

frame1 = tk.Frame(main)
frame1.pack(pady=20)

labelA = tk.Label(frame1, text="画像1")
labelA.pack(side=tk.LEFT, padx=20, pady=10)
entryA = tk.Entry(frame1, width=50)
entryA.pack(side=tk.LEFT, padx=20, pady=10)
buttonA = tk.Button(frame1, text="画像選択", command=select_and_display_image_A)
buttonA.pack(side=tk.LEFT, padx=20, pady=10)

threshold = tk.IntVar(value=50)
scale = tk.Scale(frame1, variable=threshold, orient='horizontal', from_=1, to=255, label='差分検出閾値')
scale.pack(side=tk.LEFT, padx=20, pady=10)

frame2 = tk.Frame(main)
frame2.pack(pady=20)

labelB = tk.Label(frame2, text="画像2")
labelB.pack(side=tk.LEFT, padx=20, pady=10)
entryB = tk.Entry(frame2, width=50)
entryB.pack(side=tk.LEFT, padx=20, pady=10)
buttonB = tk.Button(frame2, text="画像選択", command=select_and_display_image_B)
buttonB.pack(side=tk.LEFT, padx=20, pady=10)

match_ratio = tk.DoubleVar(value=0.2)
scale_match_ratio = tk.Scale(frame2, variable=match_ratio, orient='horizontal', from_=0.01, to=1, resolution=0.01, label='マッチ比率')
scale_match_ratio.pack(side=tk.LEFT, padx=20, pady=10)

frame3 = tk.Frame(main)
frame3.pack(pady=20)

draw_rectangle = tk.BooleanVar(value=False)
checkbutton = tk.Checkbutton(frame3, text="差分に枠を描画", variable=draw_rectangle)
checkbutton.pack(side=tk.LEFT, padx=20, pady=10)

rectangle_threshold = tk.IntVar(value=1000)
scale_rectangle_threshold = tk.Scale(frame3, variable=rectangle_threshold, orient='horizontal', from_=1, to=5000, label='枠の閾値')
scale_rectangle_threshold.pack(side=tk.LEFT, padx=20, pady=10)

button = tk.Button(main, text="実行", command=display_image)
button.pack(pady=20)

main.protocol("WM_DELETE_WINDOW", click_close)
main.mainloop()
