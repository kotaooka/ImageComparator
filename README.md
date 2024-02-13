# ImageComparator

ImageComparatorは、2つの画像を比較し、それらの間の差分を視覚化するためのPythonスクリプトです。
このスクリプトは、OpenCVとmatplotlibを使用して画像を処理し、Tkinterを使用してGUIを提供します。

## 導入
1. Pythonをインストールしてください。 https://www.python.org/downloads/
2. コマンドプロンプトから下記ライブラリをインストールしてください。
  ```
   pip install opencv-python
   pip install matplotlib
   pip install numpy
  ```
3. https://github.com/kotaooka/ImageComparator/releases から`ImageComparator.zip`をダウンロードします。
4. `ImageComparator.zip`を解凍し、好きなディレクトリに配置します。

## 使用方法
1. `ImageComparator.bat`からPythonスクリプトを実行します。
2. "画像選択"ボタンをクリックして、比較する2つの画像を選択します。
3. "差分検出閾値"スライダーを使用して、差分検出の閾値を設定します。
4. "マッチ比率"スライダーを使用して、マッチングの比率を設定します。
5. "画像比較"ボタンをクリックして、画像の比較を開始します。
6. 結果の画像が新しいウィンドウで表示されます。

## 対応している画像の拡張子
`.png` `.jpg` `.tiff`

## ユーザーインターフェース
![image](https://github.com/kotaooka/ImageComparator/assets/115392256/ae5d4db3-9480-40a3-a8a3-7e5b2d3bef07)

## 差分検出閾値スライダー
閾値スライダーを動かすと、画像差分検出に使用される二値化の閾値が変化します。
閾値は画像のピクセル値に基づいて設定され、この閾値を変更することで、画像差分の検出精度や感度が調整されます。
低い閾値はより多くの差異を検出しやすくしますが、ノイズの影響を受けやすくなります。
一方、高い閾値はより顕著な差異のみを検出しますが、細かい変化や微妙な差異は無視される可能性があります。

## マッチ比率スライダー
マッチ比率スライダーを動かすと、特徴点のマッチングに使用されるマッチ比率が変化します。
マッチ比率は特徴点の相互間の類似性を表し、この比率を変更することで、
マッチングアルゴリズムの感度やマッチングされる特徴点の数が変化します。
低いマッチ比率は多くの特徴点をマッチングさせますが、偽のマッチングが増加する可能性があります。
一方、高いマッチ比率はより信頼性の高い特徴点のみをマッチングさせますが、その数は減少します。

## 差分に枠を描画
ONにすると差分に四角い枠を描画します。
ONにした場合スライダーで枠を描画する閾値を変更することができます。

## 実行結果

### 画像の差分 （枠の描画OFF）
![Figure_1](https://github.com/kotaooka/ImageComparator/assets/115392256/c7efa06b-fac1-4aa2-902a-699b8035fcf8)

### 比較対象の画像（左右をトリミングして比較）
![body](https://github.com/kotaooka/ImageComparator/assets/115392256/016517e0-076b-426b-8cea-2501c5e519bd)

#### 引用元:サイゼリヤ2023年12月 間違い探し
`https://www.saizeriya.co.jp/entertainment/2312.html`

## ライセンス
Apache-2.0 license



