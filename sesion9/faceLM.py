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


def mouth_aspect_ratio(face):
    	# compute the euclidean distances between the two sets of
	# vertical eye landmarks (x, y)-coordinates
	A = dist.euclidean(face[61], face[67])
	B = dist.euclidean(face[63], face[65])
 
	# compute the euclidean distance between the horizontal
	# face landmark (x, y)-coordinates
	C = dist.euclidean(face[60], face[64])
 
	# compute the eye aspect ratio
	mar = (A + B) / (2.0 * C)
 
	# return the eye aspect ratio
	return mar

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-r", "--picamera", type=int, default=-1,
	help="whether or not the Raspberry Pi camera should be used")
args = vars(ap.parse_args())

# initialize dlib's face detector (HOG-based) and then create
# the facial landmark predictor
p = "shape_predictor_68_face_landmarks.dat"
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(p)

print("[INFO] camera sensor warming up...")
vs = VideoStream(usePiCamera=args["picamera"] > 0).start()
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
		# determine the facial landmarks for the face region, then
		# convert the facial landmark (x, y)-coordinates to a NumPy
		# array
		shape = predictor(gray, rect)
		shape = face_utils.shape_to_np(shape)
 
		# loop over the (x, y)-coordinates for the facial landmarks
		# and draw them on the image
		for (x, y) in shape:
			cv2.circle(frame, (x, y), 1, (0, 0, 255), -1)

		box = face_utils.rect_to_bb(rect)
		cv2.rectangle(frame,(box[0],box[1]),(box[0] + box[2],box[1] + box[3]),(0,255,0),1)
		# right eye, respectively
		upLip = shape[63,1]
		downLip = shape[67,1]
		
		mar = mouth_aspect_ratio(shape)

		cv2.putText(frame, str((box[2]*box[3])), (30,30), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255))
		(mStart, mEnd) = face_utils.FACIAL_LANDMARKS_IDXS["mouth"]



	# show the frame
	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF
 
	# if the `q` key was pressed, break from the loop
	if key == ord("q"):
		break

# do a bit of cleanup
cv2.destroyAllWindows()
vs.stop()

