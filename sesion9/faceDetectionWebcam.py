# import the necessary packages
from imutils import face_utils
from imutils.video import VideoStream
import dlib
import cv2
import datetime
import argparse
import imutils
import time
# import the necessary packages
from scipy.spatial import distance as dist


# initialize dlib's face detector (HOG-based) and then create
# the facial landmark predictor
p = "shape_predictor_68_face_landmarks.dat"
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(p)

print("[INFO] camera sensor warming up...")
vs = VideoStream().start()
time.sleep(1.0)

counter = 0
total = 0
# main loop
# loop over the frames from the video stream
while True:
	# grab the frame from the threaded video stream, resize it to
	# have a maximum width of 400 pixels, and convert it to
	# grayscale
	frame = vs.read()
	frame = imutils.resize(frame, width=400)
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
 
	# detect faces in the grayscale frame
	rects = detector(gray, 0)
	# loop over the face detections
	for rect in rects:
		box = face_utils.rect_to_bb(rect)
		cv2.rectangle(frame,(box[0],box[1]),(box[0] + box[2],box[1] + box[3]),(0,255,0),3)
		
	# show the frame
	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF
 
	# if the `q` key was pressed, break from the loop
	if key == ord("q"):
		break

# do a bit of cleanup
cv2.destroyAllWindows()
vs.stop()

