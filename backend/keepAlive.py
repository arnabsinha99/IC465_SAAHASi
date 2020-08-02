from PIL import Image
import requests
from io import BytesIO
import time


url="https://sih-heroku.herokuapp.com/api/classify"
url2="https://flask-by-senju.herokuapp.com/api/explore"
while(True):
    response = requests.get(url)
    response2= requests.get(url2)
    img = Image.open(BytesIO(response.content))
    print("on")
    # print(response2.content)
    time.sleep(60*20)
# img.show()