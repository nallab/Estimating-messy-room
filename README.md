# Estimating-messy-room
#### 本実験では、先行研究である[messy-room](https://github.com/GuanqiaoDing/messy-room-classifier)を元に行う。
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
### 追加実験2
