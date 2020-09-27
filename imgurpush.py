import pyimgur
import requests
import os
import json
import easygui
from dotenv import load_dotenv
load_dotenv()

license_plate_number = ""

CLIENT_ID = os.getenv("CLIENT_ID")
# PATH = "./license_plates/4.jpg"

# im = pyimgur.Imgur(CLIENT_ID)
# uploaded_image = im.upload_image(PATH, title="LP Finder")
# print(uploaded_image.link)



def pushImage(image_Location):
    #print('pushing')
    path = "./plate_copies/{}".format(image_Location)
    im = pyimgur.Imgur(CLIENT_ID)
    uploaded_image = im.upload_image(path, title="LP Finder")
    print(f"Image ID: {os.path.splitext(os.path.basename(uploaded_image.link))[0]}")
    sendToServer((os.path.splitext(os.path.basename(uploaded_image.link))[0]))


def sendToServer(id):
    url = f'http://34.75.252.241:3000/api/getLP/{id}'
    r = requests.get(url)
    print(r.text)
    
    license_plate_number = json.loads(r.text)['license_plate']
    easygui.msgbox(f'License Plate found: {license_plate_number}', title="License Alert")
