import pyimgur

CLIENT_ID = ""
PATH = "./license_plates/4.jpg"

im = pyimgur.Imgur(CLIENT_ID)
uploaded_image = im.upload_image(PATH, title="LP Finder")
print(uploaded_image.link)
