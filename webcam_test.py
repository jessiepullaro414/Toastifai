#this is a project made at hackriddle 2016
#it is a "smart" toaster using clarifai, simplecv, and twilio
#by: Jessie Pullaro, Frank Calas, Max Farrel and Kyle Spomer


from PIL import Image, ImageEnhance
import cv2

# Camera 0 is the integrated web cam on my netbook
camera_port = 1

#Number of frames to throw away while the camera adjusts to light levels
ramp_frames = 30

#Number of images taken
img_count = 0

# Now we can initialize the camera capture object with the cv2.VideoCapture class.
# All it needs is the index to a camera port.
camera = cv2.VideoCapture(camera_port)

# Captures a single image from the camera and returns it in PIL format
def get_image():
 # read is the easiest way to get a full image out of a VideoCapture object.
 retval, im = camera.read()
 return im

# Takes in the current number of images and makes a string for the next location/name
def image_name(counter):
    file = "/home/jessie/Projects/hackathons/toast/Toastifai/notimages/" + str(counter) + ".png"
    return file

# Ramp the camera - these frames will be discarded and are only used to allow v4l2
# to adjust light levels, if necessary

#print("Warming Engine...")
#for i in xrange(ramp_frames):
# temp = get_image()
#print("*CLICK*")

# Loop for taking images
while (img_count < 80):
    # Take the actual image we want to keep
    camera_capture = get_image()

    # Make name of the file and incriments the counter
    file = image_name(img_count)
    img_count += 1

    ## File = "/home/pinheadqt/Documents/bs_directory/Toastifai/test_image.png"
    # A nice feature of the imwrite method is that it will automatically choose the
    # correct format based on the file extension you provide. Convenient!
    cv2.imwrite(file, camera_capture)

    #PIL stuff
    img = Image.open(file)
    converter = ImageEnhance.Color(img)
    img2 = converter.enhance(2.0)
    img2.save(file)



# You'll want to release the camera, otherwise you won't be able to create a new
# capture object until your script exits
del(camera)


#from PIL import Image, ImageEnhance
#img = Image.open('bus.png')
#converter = ImageEnhance.Color(img)
#img2 = converter.enhance(2.0)
#img2.save("bus2.png")
