"""
Step 1: Get a lot of car images
Step 2: Turn them into grayscale (black n white)
This makes the algorithm faster
Step 3: Train the algorithm to detect cars and pedestrians
We use Haar Features to do this


"""
import cv2

# Our image
img_file = 'car image.jpg'
video = cv2.VideoCapture('Tesla.mp4')

# Our pre-trained car classifier
classifier_file = "car_detector.xml"

while True:

    # Read the current frame (1st part is boolean, 2nd is array of coordinates)
    (read_successful, frame) = video.read()

    # safe coding
    if read_successful:
        # convert to grayscale
        grayscale_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    else:
        break

    # Display the image with the cars spotted
    cv2.imshow("Subhro's car detector", grayscale_frame)

    # Dont autoclose( Wait for a key press )
    cv2.waitKey(1)

"""
# Create opencv image
# Reads the pixel data from image
img = cv2.imread(img_file)

# convert image to grayscale
black_n_white = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


# Create car haar cascade classifier
car_tracker = cv2.CascadeClassifier(classifier_file)

# detect cars of any scale
# stores coordinates which we will use to draw rectangles
cars = car_tracker.detectMultiScale(black_n_white)

# Draw rectangles around the cars

for (x, y, w, h) in cars:
    cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,255),2)




"""

print ("code complete")
