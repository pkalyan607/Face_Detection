from mtcnn import MTCNN
import cv2 as cv

detector = MTCNN()

img = cv.imread('mega_family_3.jpg')

output = detector.detect_faces(img)
print(output)

for i in output:

    x, y, width, height = i['box']

    left_eyeX, left_eyeR = i['keypoints']['left_eye']
    right_eyeX, right_eyeR = i['keypoints']['right_eye']
    nose_X,nose_Y = i['keypoints']['nose']
    left_mouth_X, left_mouth_R = i['keypoints']['mouth_left']
    right_mouth_X, right_mouth_R = i['keypoints']['mouth_right']

    cv.rectangle(img, pt1=(x, y), pt2=(x+width, y+height), color=(0, 0, 255), thickness=3)
    cv.circle(img, center=(left_eyeX, left_eyeR), radius=5, color=(0, 0, 255),thickness=3)
    cv.circle(img, center=(right_eyeX, right_eyeR), radius=5, color=(0, 0, 255),thickness=3)
    cv.circle(img, center=(nose_X, nose_Y), radius=5, color=(0, 0, 255),thickness=3)
    cv.circle(img, center=(left_mouth_X, left_mouth_R), radius=5, color=(0, 0, 255),thickness=3)
    cv.circle(img, center=(right_mouth_X, right_mouth_R), radius=5, color=(0, 0, 255),thickness=3)

cv.imshow('Mega-Family', img)

cv.waitKey(0)
