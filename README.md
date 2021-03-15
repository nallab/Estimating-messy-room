# Estimating-messy-room
#### 本実験では、先行研究である[messy-room](https://github.com/GuanqiaoDing/messy-room-classifier)を元に行う。
#### 使用する画像は[kaggleデータセット](https://www.kaggle.com/cdawn1/messy-vs-clean-room)を用いる。
## 実験手順
### 予備実験
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

### 追加実験1
#### スクレイピングを用いて画像を収集し、データセットを作成し、モデルの精度を検証する。
```
img_download.py
```
#### 収集した画像に対してのラベル付与を行う。今回はゼミのメンバーにアンケートを行い集計しその結果からラベルを付与します。

### 追加実験2
#### Grad-CAMを用いて、特徴抽出の際の重みを可視化する。
```
keras-grad.py
```
