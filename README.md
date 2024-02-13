# ImageComparator

ImageComparatorは、2つの画像を比較し、それらの間の差分を視覚化するためのPythonスクリプトです。このスクリプトは、OpenCVとmatplotlibを使用して画像を処理し、Tkinterを使用してGUIを提供します。

## 必要なパッケージ
Python 3.x
OpenCV
Matplotlib
NumPy
tkinter

## 使用方法
1. batファイルからスクリプトを実行します。GUIが表示されます。
2. "画像選択"ボタンをクリックして、比較する2つの画像を選択します。
3. "差分検出閾値"スライダーを使用して、差分検出の閾値を設定します。
4. "マッチ比率"スライダーを使用して、マッチングの比率を設定します。
5. "画像比較"ボタンをクリックして、画像の比較を開始します。
6. 結果の画像が新しいウィンドウで表示されます。

## 差分検出閾値スライダー:
閾値スライダーを動かすと、画像差分検出に使用される二値化の閾値が変化します。
閾値は画像のピクセル値に基づいて設定され、この閾値を変更することで、画像差分の検出精度や感度が調整されます。
低い閾値はより多くの差異を検出しやすくしますが、ノイズの影響を受けやすくなります。
一方、高い閾値はより顕著な差異のみを検出しますが、細かい変化や微妙な差異は無視される可能性があります。

## マッチ比率スライダー:
マッチ比率スライダーを動かすと、特徴点のマッチングに使用されるマッチ比率が変化します。
マッチ比率は特徴点の相互間の類似性を表し、この比率を変更することで、
マッチングアルゴリズムの感度やマッチングされる特徴点の数が変化します。
低いマッチ比率は多くの特徴点をマッチングさせますが、偽のマッチングが増加する可能性があります。
一方、高いマッチ比率はより信頼性の高い特徴点のみをマッチングさせますが、その数は減少します。

## 差分に枠の描画
ONにすると差分に四角い枠を描画します。ONにした場合スライダーで閾値を変更することができます。
