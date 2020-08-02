import time

start =time.clock()
import warnings
warnings.filterwarnings("ignore")
import sys
# sys.path.append('../')    
sys.path.insert(1, 'leaf-image-segmentation-master')
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline
import torchvision
import torch
from torch import nn, optim
import random
from torchvision import datasets
# import albumentations as A
import os
import fastai
from fastai.vision import *
from fastai.metrics import error_rate,accuracy,fbeta 
from segment import segment_leaf
BATCH_SIZE = 64

# start =time.clock()



x = ['Apple___Apple_scab','Apple___Black_rot','Apple___Cedar_apple_rust', 'Apple___healthy',
     'Cherry_(including_sour)___healthy','Cherry_(including_sour)___Powdery_mildew','Potato___Early_blight',
     'Potato___healthy','Potato___Late_blight']

# print("model export2")
model_name='export2.pkl' #resnet50
model_dir=os.getcwd()+ "/ignore"

learn = load_learner(model_dir,model_name)

print("File Name \t\t\t Prediction")
print("--------------------------------------------------------------------")
m1=[]
y=os.listdir('./test')
# print(y)
for fname in y:

    img=open_image(os.path.join('./test/',fname))
    pred,pred_idx,probs = learn.predict(img)
    # print(fname,"\t\t\t",x[pred_idx])
    wito=x[pred_idx]
    wth=pred
    if(wito=='Apple___Black_rot'):
        original, output_image =segment_leaf(os.path.join('./test/',fname), "flood", False, 0)
        img=open_image('testing.jpg')
    # img.show()
    
        pred,pred_idx,probs = learn.predict(img)
    # if(wito != x[pred_idx]):
    print(fname,"\t\t\t",x[pred_idx])
    # m1.append(x[pred_idx])
    # print(fname,x[pred_idx],pred,probs)
    # print(fname,pred,pred_idx,probs)
   


# img1=open_image('./test/Apple_BlackRot1.JPG')
# pred,pred_idx,probs = learn.predict(img1)
# print("ah1","\t\t\t",x[pred_idx])
# # img1=open_image('./test/cpm1.jpg')
# pred,pred_idx,probs = learn.predict(img1)
# print("cpm1","\t\t\t",x[pred_idx])
el=time.clock()-start
print(el)

# fname='cdr.jpg'
# img=open_image(os.path.join('./test/',fname))
# pred,pred_idx,probs = learn.predict(img)
# print(fname,"\t\t\t",x[pred_idx])

# original, output_image =segment_leaf(os.path.join('./test/',fname), "flood", False, 0)
# img=open_image('testing.jpg')


# model_name='export2.pkl'
# model_dir=os.getcwd()+ "/ignore"

# learn = load_learner(model_dir,model_name)

# # img1=open_image('./test/ah1.jpg')
# # pred,pred_idx,probs = learn.predict(img1)
# # print("ah1","\t\t\t",x[pred_idx])
# # img1=open_image('./test/cpm1.jpg')
# # pred,pred_idx,probs = learn.predict(img1)
# # print("cpm1","\t\t\t",x[pred_idx])


# # fname='cdr.jpg'
# # img=open_image(os.path.join('./test/',fname))
# # pred,pred_idx,probs = learn.predict(img)
# # print(fname,"\t\t\t",x[pred_idx])

# # original, output_image =segment_leaf(os.path.join('./test/',fname), "flood", False, 0)
# # img=open_image('testing.jpg')

# m2=[]
# y=os.listdir('./test')
# # print(y)
# for fname in y:

#     img=open_image(os.path.join('./test/',fname))
#     pred,pred_idx,probs = learn.predict(img)
#     # print(fname,"\t\t\t",x[pred_idx])
#     wito=x[pred_idx]
#     wth=pred
#     if(wito=='Apple___Black_rot'):
#         original, output_image =segment_leaf(os.path.join('./test/',fname), "flood", False, 0)
#         img=open_image('testing.jpg')
#     # img.show()
    
#         pred,pred_idx,probs = learn.predict(img)
#     # if(wito != x[pred_idx]):
#     # print(fname,"\t\t",x[pred_idx])
#     m2.append(x[pred_idx])

#     # print(fname,x[pred_idx],pred,probs)
#     # print(fname,pred,pred_idx,probs)
   
# for i in range(len(m1)):
#     # if(m1[i]!=m2[i]):
#     print(y[i],"\t\t\t",m1[i],"\t\t\t",m2[i])
    

# # print("\nmodel export (1-1)")
# # model_name='export1-1.pkl'
# # model_dir=os.getcwd()+ "/ignore"

# # learn = load_learner(model_dir,model_name)


# # y=os.listdir('./test')
# # # print(y)
# # for fname in y:
# #     img=open_image(os.path.join('./test/',fname))
# #     pred,pred_idx,probs = learn.predict(img)
# #     print(fname,"\t\t\t",x[pred_idx])