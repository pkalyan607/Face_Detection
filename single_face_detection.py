from mtcnn import MTCNN
import tensorflow
import cv2 as cv

# object creation
detector = MTCNN()

# reading image
img = cv.imread("pawankalyan.jpg")

# Output of detection face
output = detector.detect_faces(img)
print(output)

# co-ordinates of bounding box
x, y, width, height = output[0]['box']

# Bounding box
cv.rectangle(img, pt1=(x, y), pt2=(x+width, y+height), color=(255, 0, 0), thickness=2)
cv.imshow("Image", img)

cv.waitKey(0)
