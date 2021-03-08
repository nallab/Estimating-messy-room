# Estimating-messy-room
## 実験手順
### まずは特徴抽出を行う。ImageNetの重みを使用したXceptionモデルを用いてデータセットの画像から特徴を抽出します。
```
python aug_and_feature_extract.py
```
### その後、各画像に対応したラベルと抽出した特徴を用いて識別層の学習を行います。
```
python retrain.py
```
