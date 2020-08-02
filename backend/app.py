from flask import Flask,jsonify,request,send_file

app = Flask(__name__)



import warnings
warnings.filterwarnings("ignore")

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
from io import BytesIO
from typing import List, Dict, Union, ByteString, Any
import requests
from thresh import marked
from PIL import Image
import base64

BATCH_SIZE = 64



x = ['Apple___Apple_scab','Apple___Black_rot','Apple___Cedar_apple_rust', 'Apple___healthy',
     'Cherry_(including_sour)___healthy','Cherry_(including_sour)___Powdery_mildew','Potato___Early_blight',
     'Potato___healthy','Potato___Late_blight']


model_name='export.pkl'
model_dir=os.getcwd()+ "/models"

learn = load_learner(model_dir,model_name)
# img=open_image('appleext.jpg')
# pred,pred_idx,probs = learn.predict(img)
# print(x[pred_idx])


# def image2np(image:Tensor)->np.ndarray:
#     "Convert from torch style `image` to numpy/matplotlib style."
#     res = image.cpu().permute(1,2,0).numpy()
#     return res[...,0] if res.shape[2]==1 else res

def encode_img():
    images=[]
    image = open('spot.jpg', 'rb')
    image_read = image.read()
    image_64_encode = base64.encodestring(image_read).decode('utf-8')
    images.append(image_64_encode)

    image = open('no_spots.jpg', 'rb')
    image_read = image.read()
    image_64_encode = base64.encodestring(image_read).decode('utf-8')
    images.append(image_64_encode)


    image = open('gray.jpg', 'rb')
    image_read = image.read()
    image_64_encode = base64.encodestring(image_read).decode('utf-8')
    images.append(image_64_encode)


    return images

def load_model(path="../", model_name="export1.pkl"):
    learn = load_learner(path, fname=model_name)
    return learn


def load_image_url(url: str) -> Image:
    response = requests.get(url)
    img = open_image(BytesIO(response.content))
    return img


def load_image_bytes(raw_bytes: ByteString) -> Image:
    img = open_image(BytesIO(raw_bytes))
    return img


def predict(img, n: int = 3) -> Dict[str, Union[str, List]]:
    pred,pred_idx,probs = learn.predict(img)
    # print(type(img))
    # numim=image2np(img)

    # marked(numim)
    return {"predictions": x[pred_idx]}


@app.route('/api/getSpot', methods=['GET'])
def getSpot():
    return send_file('spot.jpg', mimetype='image/jpeg')

@app.route('/api/getNoSpot', methods=['GET'])
def getNoSpot():
    return send_file('no_spots.jpg', mimetype='image/jpeg')

@app.route('/api/getGray', methods=['GET'])
def getGray():
    return send_file('gray.jpg', mimetype='image/jpeg')


@app.route('/api/classify', methods=['POST', 'GET'])
def upload_file():
    if request.method == 'POST':
        bytes = request.files['file'].read()
        img = load_image_bytes(bytes)
        image = Image.open(io.BytesIO(bytes))
        image.save("to_mark.jpg")
        marked()
        images=encode_img()
        res = [predict(img),images]
    else:
        return send_file(attachment_filename='wah.jpeg', mimetype='image/jpeg')
    return jsonify(res)
    

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'prdiction': x[pred_idx]})

if __name__ == '__main__':
    app.run(debug=True)




    # pred_class, pred_idx, outputs = learn.predict(img)
    # pred_probs = outputs / sum(outputs)
    # pred_probs = pred_probs.tolist()
    # predictions = []
    # for image_class, output, prob in zip(model.data.classes, outputs.tolist(), pred_probs):
    #     output = round(output, 1)
    #     prob = round(prob, 2)
    #     predictions.append(
    #         {"class": image_class.replace("_", " "), "output": output, "prob": prob}
    #     )

    # predictions = sorted(predictions, key=lambda x: x["output"], reverse=True)
    # predictions = predictions[0:n]
    # return {"class": str(pred_class), "predictions": predictions}




    # if request.method == 'GET':
    #     url = request.args.get("url")
    #     img = load_image_url(url)
    # else:
    #     bytes = request.files['file'].read()
    #     img = load_image_bytes(bytes)