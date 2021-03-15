from keras.preprocessing.image import ImageDataGenerator
from keras.applications.xception import Xception
import numpy as np
import csv
from sklearn.model_selection import train_test_split

# load data
#(x_train, y_train), (x_val, y_val) = np.load('data/room_dataset.npy')#add allow_pickle=True
(x_train, y_train), (x_val, y_val) = np.load('data/room_dataset.npy', allow_pickle=True)
ex = np.load('data/images.npy')
ey = np.load('data/label.npy')
x_train2,x_val2,y_train2,y_val2 = train_test_split(ex, ey, train_size=0.8, random_state=1)

new_xt = np.vstack([x_train, x_train2])
new_yt = np.concatenate([y_train, y_train2])
new_xv = np.vstack([x_val, x_val2])
new_yv = np.concatenate([y_val, y_val2])

#print(new_yt.shape)

# normalize data
"""
channel_mean = np.mean(x_train, axis=(0, 1, 2))
channel_std = np.std(x_train, axis=(0, 1, 2))
"""
channel_mean =  np.mean(new_xt, axis=(0,1,2))
channel_std = np.std(new_xt, axis=(0,1,2))
# mean, std calculated here are also used in predicting test images: predict.py

"""
channel_mean = np.array([110.73151039, 122.90935242, 136.82249855])
channel_std = np.array([69.39734207, 67.48444001, 66.66808662])
"""
#x_train = x_train.astype('float32')
new_xt = new_xt.astype('float32')
#x_val = x_val.astype('float32')
new_xv = new_xv.astype('float32')
#x_train2 = x_train2.astype('float32')
#x_val2 = x_val2.astype('float32')
"""
for i in range(3):
    x_train[:, :, :, i] = (x_train[:, :, :, i] - channel_mean[i]) / channel_std[i]
    x_val[:, :, :, i] = (x_val[:, :, :, i] - channel_mean[i]) / channel_std[i]
"""
for i in range(3):
    new_xt[:,:,:,i] = (new_xt[:,:,:,i] - channel_mean[i]/channel_std[i])
    new_xv[:,:,:,i] = (new_xv[:,:,:,i] - channel_mean[i]/channel_std[i])

# define data augmentation
datagen = ImageDataGenerator(
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True
)

#augmented_data = x_train.copy()
augmented_data = new_xt.copy()
#train_labels = y_train.copy()
train_labels = new_yt.copy()

# flow in advance, get augmented training data and corresponding labels
for i in range(19):
    #for img, label in datagen.flow(x_train, y_train, batch_size=192):
    #for img, label in datagen.flow(x_train2, y_train2, batch_size=192):
    for img, label in datagen.flow(new_xt, new_yt, batch_size=192):
        #print(i)
        augmented_data = np.vstack((augmented_data, img))
        #print(augmented_data.shape)
        train_labels = np.hstack((train_labels, label))
        #print(train_labels.shape)
        break

# pre-trained model to extract features
base_model = Xception(include_top=False, weights='imagenet', pooling='avg')
train_features = base_model.predict(augmented_data)
np.savetxt('data/train_features3.csv', train_features, fmt='%.5f', delimiter=',')
np.savetxt('data/train_labels3.csv', train_labels, fmt='%1d', delimiter=',')

# save validation features and label
#val_features = base_model.predict(x_val)
val_features = base_model.predict(new_xv)
np.savetxt('data/val_features3.csv', val_features, fmt='%.5f', delimiter=',')
#np.savetxt('data/val_labels2.csv', y_val, fmt='%1d', delimiter=',')
np.savetxt('data/val_labels3.csv', new_yv, fmt='%1d', delimiter=',')

