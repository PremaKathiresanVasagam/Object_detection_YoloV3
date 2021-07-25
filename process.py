# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 08:39:24 2021

@author: EPK6KOR
"""

import os
from random import shuffle
from math import floor
os.chdir(r"D:\AI\Assignments\EV\YoloV3\data\customdata")

#Step1: Fetch image names and create a list
def get_file_list_from_dir(datadir):
    all_files = os.listdir(os.path.abspath(datadir))
    data_files = list(filter(lambda file: file.endswith('.txt'), all_files))
    return data_files

file_list_txt = get_file_list_from_dir(r'D:\AI\Assignments\EV\Jupyternotebooks\JSON2YOLO-master\new_dir\labels\bbox-annotations')

#Step2: Change .txt to .jpg
file_list = []
for f in file_list_txt:
    name = f.split(".")[0]
    name = './data/customdata/images/' + name + '.jpg'
    #print(name)
    file_list.append(name)


#Step3: Randomize the files
def randomize_files(file_list):
    shuffle(file_list)

#Step4: Split into train, val and test data
def get_training_and_testing_sets(file_list, split = 0.7):
    randomize_files(file_list) 
    split_index = floor(len(file_list) * split)
    training = file_list[:split_index]
    testing = file_list[split_index:]
    return training, testing

training, testing = get_training_and_testing_sets(file_list, split = 0.90)
#validation, testing = get_training_and_testing_sets(val_test, split = 0.98)


file_name_jpg = []
for f in file_list:
    name = f.split(".")[0]
    name = name + '.jpg'
    #print(name)
    file_name_jpg.append(name)



with open("training.txt", 'w') as file:
        for row in training:
            s = "".join(map(str, row))
            file.write(s+'\n')
            

with open("testing.txt", 'w') as file:
        for row in testing:
            s = "".join(map(str, row))
            file.write(s+'\n')

#Get the image resolution
import cv2
#import glob
os.chdir(r"D:/AI/Assignments/EV/Data/trainval/images/")

filenames = [img.split('/')[-1] for img in training]

images = []
with open("training_shapes.txt", 'w') as file:
    for img in filenames:
        n= cv2.imread(img)
        width, height = n.shape[1], n.shape[0]
        file.write("{} {}".format(width,height))
        file.write('\n')
