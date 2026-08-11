import os
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from skimage.color import rgb2gray
import helper

def process(directoryName):
    for filename in os.listdir(directoryName):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            filenamestr = filename.split('.')[0]
            # matplotlib recommends using pillows Image() import. Trying to instead use matplotlib direct will get a `SyntaxError: expected png file`
            # this code was historically using scikits methods which are now deprecated
            # see https://matplotlib.org/stable/tutorials/images.html
            img = Image.open(os.path.join(directoryName, filename))
            img_new = rgb2gray(img)
            plt.imshow(img_new)
            plt.title('Grayscale Format') 
            plt.imsave(os.getcwd() + "/output/" + filenamestr +"-" + helper.generateRandomName() + "_modified.jpeg", (img_new*255).astype(np.uint8))
        else:
            continue