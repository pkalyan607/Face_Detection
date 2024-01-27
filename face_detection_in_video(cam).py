import cv2 as cv
from mtcnn import MTCNN

# we have to pass parameter which camera video should display
cap = cv.VideoCapture(0)
detector = MTCNN()

while True:

    ret, frame = cap.read()
    output = detector.detect_faces(frame)

    for single_output in output:
        x, y, width, height = single_output['box']
        cv.rectangle(frame, pt1=(x, y), pt2=(x+width, y+height), color=(255, 0, 0), thickness=3)
    cv.imshow('window_cam', frame)

    if cv.waitKey(1) & 0xFF == ord('x'):
        break

cv.destroyAllWindows()