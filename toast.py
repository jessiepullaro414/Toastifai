#this is a project made at hackriddle 2016
#it is a "smart" toaster using clarifai, simplecv, and twilio
#by: Jessie Pullaro, Frank Calas, Max Farrel and Kyle Spomer





from clarifai import rest
from clarifai.rest import ClarifaiApp


#pulls the api keys from keys.py
app = ClarifaiApp("nnDJHbfgjR6qFYT_zv9RVoMBmR9-vFnvWFMHfm0F", "JqEgorhvy0DGV8PYHwhDg24f3N4yGiRi1HQBS46a")

'''
# import 80 images to train what toast is
for it in range(10,69):
    app.inputs.create_image_from_filename("/home/jessie/Projects/hackathons/toast/Toastifai/images/{0}.png".format(str(it)), concepts=["perfect toast"], not_concepts=["not toast"])


# import 80 images to train what toast is not
for i in range(0,79):
    app.inputs.create_image_from_filename("/home/jessie/Projects/hackathons/toast/Toastifai/notimages/{0}.png".format(str(i)), concepts=["not toast"], not_concepts=["perfect toast"])


model = app.models.create(model_id="toast", concepts=["not toast", "perfect toast"])

model = model.train()
'''

model = app.models.get("toast")

# predict with samples
print model.predict_by_filename("/home/jessie/Projects/hackathons/toast/Toastifai/infiniteimages/68.png")
