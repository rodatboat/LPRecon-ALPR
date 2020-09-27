import pyimgur
import os
from dotenv import load_dotenv
load_dotenv()

CLIENT_ID = os.environ['CLIENT_ID']
PATH = "./license_plates/fake.jpg"

im = pyimgur.Imgur(CLIENT_ID)
uploaded_image = im.upload_image(PATH, title="LP Finder")
print(uploaded_image.link)
