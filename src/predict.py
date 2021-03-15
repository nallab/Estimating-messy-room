from keras.applications.xception import Xception
from keras.models import load_model
from glob import glob
import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
import os

# pre-process test images
import preprocessing
test_dir = './images/all'
#test_dir = './images/new_test'
#test_dir = './images/bad_predict'
#test_dir = './images/test'


filenames = glob(os.path.join(test_dir, '*.png'))

for i, file in enumerate(filenames):
    #print('processing:', file)
    img = cv.imread(file)
    resized = preprocessing.resize(img)
    img_name = str(i) + '.png'
    #filepath = os.path.join('./images/test_buf', img_name)
    filepath = os.path.join('./images/all_resize', img_name)
    cv.imwrite(filepath, resized)
"""
def load_test_images(file_list):
    test_set = list()
    test_set_rgb = list()
    for file in file_list:
        #print(file)
        img = cv.imread(file)
        img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        test_set.append(img)
        test_set_rgb.append(img_rgb)

    return np.asarray(test_set), np.asarray(test_set_rgb)

test_dir = './images/test_buf'

filenames = glob(os.path.join(test_dir, '*.png'))
images, images_rgb = load_test_images(filenames)

# calculate from the training set
#channel_mean =  np.mean(images, axis=(0,1,2))
#channel_std =  np.std(images, axis=(0,1,2))
channel_mean = np.array([150.57611687, 139.12877504, 128.64689842])
channel_std = np.array([68.35155918, 68.5150119, 71.80614674])
#channel_mean = np.array([150.46023984, 138.4656352,  128.66298491])
#channel_std = np.array([68.90541871, 68.99196688, 71.61083242])
#channel_mean = [144.99534654, 133.11671137, 124.13454665]
#channel_std = [70.68313338, 70.57243075, 73.01061004]
# normalize images
images = images.astype('float32')
for j in range(3):
    images[:, :, :, j] = (images[:, :, :, j] - channel_mean[j]) / channel_std[j]

#make predictions
base_model = Xception(include_top=False, weights='imagenet', pooling='avg')
room_model = load_model('./model/room_model_1552970840.h5')#org
#room_model = load_model('./model/room_model_1612096616.h5')#retrain
#room_model = load_model('./model/room_model_1611767147.h5')#org+retrain
#room_model = load_model('./model/room_model_1612451812.h5')#remove badpredict
#room_model = load_model('./model/room_model_1612457790.h5')#remove all_noize
#room_model = load_model('./model/room_model_1612473132.h5')#clean = messy
features = base_model.predict(images)
predictions = room_model.predict(features)

#plot results
fig = plt.figure()
fig.suptitle('predict result', size=15, weight='bold')
fig.subplots_adjust(hspace=0.3, wspace=0.2)
save_dir = os.path.join('./all_result','result_revenge')
os.makedirs(save_dir, exist_ok = True)
for i in range(len(images)):
    ax = fig.add_subplot(1, 1, 1)
    #ax = fig.add_subplot(3, 4, i+1)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.imshow(images_rgb[i], aspect='auto')
    #ax.imshow(images_rgb[l])
    result = 'Messy: {:.2f}'.format(predictions[i][0])
    ax.set_xlabel(result, color='g', size=10, weight='bold', horizontalalignment='center')
    #plt.savefig('./all_result/result{0}'.format(l))
    plt.savefig(os.path.join(save_dir,'result{0}'.format(i)))
#plt.show()

"""
