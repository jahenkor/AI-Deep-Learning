import numpy as np
import matplotlib.pyplot as plt
import os
import cv2
from tqdm import tqdm

DATADIR = "~/Development/PythonProgramTuts/Datasets/PetImages" #Can be found: https://www.microsoft.com/en-us/download/confirmation.aspx?id=54765

CATEGORIES = ["Dog","Cat"]

for category in CATEGORIES: # do dogs and cats
    path = os.path.join(DATADIR,category) # create path to dogs and cats
    for img in os.listdir(path):
        img_array = cv2.imread(os.path.join(path,img) ,cv2.IMREAD_GRAYSCALE) # convert to array
        plt.imshow(img_array, cmap='gray') # graph it
        plt.show() # display!

        break
    break
