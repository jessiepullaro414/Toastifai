#this is a project made at hackriddle 2016
#it is a "smart" toaster using clarifai, simplecv, and twilio
#by: Jessie Pullaro, Frank Calas, Max Farrel and Kyle Spomer

from clarifai import rest
from clarifai.rest import ClarifaiApp


file = "current_image.png"


camera_port = 1
# Now we can initialize the camera capture object with the cv2.VideoCapture class.
# All it needs is the index to a camera port.
camera = cv2.VideoCapture(camera_port)
#pulls the api keys from keys.py
app = ClarifaiApp("nnDJHbfgjR6qFYT_zv9RVoMBmR9-vFnvWFMHfm0F", "JqEgorhvy0DGV8PYHwhDg24f3N4yGiRi1HQBS46a")

model = app.models.get("toast")

toast_perfect = 0

# predict with samples

def get_image():
 # read is the easiest way to get a full image out of a VideoCapture object.
 retval, im = camera.read()
 return im


while (toast_perfect < .75):
    camera_capture = get_image()

    cv2.imwrite(file, camera_capture)
    #PIL stuff
    img = Image.open(file)
    converter = ImageEnhance.Color(img)
    img2 = converter.enhance(2.0)
    img2.save(file)


    model_json = model.predict_by_filename(file)


    if (model_json[u'outputs'][0][u'data'][u'concepts'][0][u'id'] == "perfect toast"):
        toast_perfect = model_json[u'outputs'][0][u'data'][u'concepts'][0][u'value']



"""
has to loop and get pictures
send to api
take in the thingy
when it gets to a threshold of perfect
"""
