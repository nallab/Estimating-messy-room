from keras.applications.xception import Xception
import pandas as pd
import numpy as np
import cv2
from keras import backend as K
from keras.preprocessing.image import array_to_img, img_to_array, load_img
from keras.models import load_model
import glob
import pprint
import os

def Grad_Cam(input_model, x, layer_name):
    X = np.expand_dims(x,axis=0)
    X = X.astype('float32')
    preprocessed_input = X / 255.0
    #preprocessed_input = x / 255.0

    predictions = model.predict(preprocessed_input)
    class_idx = np.argmax(predictions[0])
    class_output = model.output[:,class_idx]

    conv_output = model.get_layer(layer_name).output
    grads = K.gradients(class_output, conv_output)[0]
    gradient_function = K.function([model.input], [conv_output, grads])
    output, grads_val = gradient_function([preprocessed_input])
    output, grads_val = output[0], grads_val[0]

    weights = np.mean(grads_val, axis=(0,1))
    cam = np.dot(output, weights)
    
    cam = cv2.resize(cam, (299,299), cv2.INTER_LINEAR)
    cam = np.maximum(cam, 0)
    cam = cam / cam.max()
    
    jetcam = cv2.applyColorMap(np.uint8(255*cam), cv2.COLORMAP_JET)
    jetcam = cv2.cvtColor(jetcam, cv2.COLOR_BGR2RGB)
    jetcam = (np.float32(jetcam) + x/2)
    
    return jetcam

if __name__ == '__main__':
    model = Xception(include_top=False, weights='imagenet', pooling='avg')
    model.summary()
    all_path = glob.glob('./images/*')
    layer_name = [l.name for l in model.layers]
    lay = 'global_average_pooling2d_1'
    #pprint.pprint(layer_name)
    #os.makedirs('./sample', exist_ok=True)
    for i, path in enumerate(all_path):
        path_result = os.path.join(path , 'grad_result2')
        print(path)
        os.makedirs(path_result,exist_ok=True)
        img_path = glob.glob(path+'/*.png')
        for l,img in enumerate(img_path):
            x = img_to_array(load_img(img,target_size=(299,299)))
            image = Grad_Cam(model,x,lay)
            array_to_img(image)
            out_path = os.path.join(path_result, 'output_{0}.png'.format(l))
            cv2.imwrite(out_path, image)
