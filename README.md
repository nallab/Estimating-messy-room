# Estimating-messy-room
#### 本実験では、先行研究である[messy-room](https://github.com/GuanqiaoDing/messy-room-classifier)を元に行う。
#### 使用する画像は[kaggleデータセット](https://www.kaggle.com/cdawn1/messy-vs-clean-room)を用いる。
## 実験手順
### 1.予備実験
#### まずは特徴抽出を行う。ImageNetの重みを使用したXceptionモデルを用いてデータセットの画像から特徴を抽出します。
```
python aug_and_feature_extract.py
```
#### その後、各画像に対応したラベルと抽出した特徴を用いて識別層の学習を行います。
```
python retrain.py
```
#### 識別層の学習後、予測したい部屋の画像の特徴を抽出させ予測を行います。
```
python predict.py
```

### 2.追加実験1
#### スクレイピングを用いて画像を収集し、データセットを作成し、モデルの精度を検証する。
```
python img_download.py
```
#### 収集した画像をnumpy配列に変換し、npyファイルとして保存する。対象の画像をobj以下に置き実行
```
python convert_img_to_array.py
```
#### 収集した画像に対してのラベル付与を行う。今回はゼミのメンバーにアンケートを行い集計しその結果からラベルを付与します。アンケートはgoogleスプレッドシートで行い結果をcsvファイルにして出力します。その後に、集計を行います。totalにアンケート結果のcsvファイルを置きtotal.pyを実行する
```
python total.py
```

### 3.追加実験2
#### Grad-CAMを用いて、特徴抽出の際の重みを可視化する。images以下に対象の画像を置き実行する
```
python keras-grad.py
```
