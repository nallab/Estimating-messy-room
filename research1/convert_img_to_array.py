import numpy as np
from PIL import Image
import glob
import cv2
from natsort import natsorted

all_path = natsorted(glob.glob('./obj_img/*.png'))
img_array = []

for i, path in enumerate(all_path):
    img = Image.open(path)
    img_resize = img.resize((299,299))
    img_array.append(np.array(img_resize))

img_np = np.array(img_array)
print(img_np.shape)
np.save('./images', img_np)

