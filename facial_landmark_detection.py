from mtcnn import MTCNN
import cv2 as cv

detector = MTCNN()

img = cv.imread('pawankalyan.jpg')

output = detector.detect_faces(img)
print(output)

x, y, width, height = output[0]['box']

left_eyeX, left_eyeR = output[0]['keypoints']['left_eye']
right_eyeX, right_eyeR = output[0]['keypoints']['right_eye']
nose_X,nose_Y = output[0]['keypoints']['nose']
left_mouth_X, left_mouth_R = output[0]['keypoints']['mouth_left']
right_mouth_X, right_mouth_R = output[0]['keypoints']['mouth_right']

cv.rectangle(img, pt1=(x, y), pt2=(x+width, y+height), color=(0, 0, 255), thickness=2)
cv.circle(img, center=(left_eyeX, left_eyeR), radius=5, color=(0, 0, 255),thickness=3)
cv.circle(img, center=(right_eyeX, right_eyeR), radius=5, color=(0, 0, 255),thickness=3)
cv.circle(img, center=(nose_X, nose_Y), radius=5, color=(0, 0, 255),thickness=3)
cv.circle(img, center=(left_mouth_X, left_mouth_R), radius=5, color=(0, 0, 255),thickness=3)
cv.circle(img, center=(right_mouth_X, right_mouth_R), radius=5, color=(0, 0, 255),thickness=3)

cv.imshow('PawanKalyan', img)

cv.waitKey(0)
