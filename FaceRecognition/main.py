import cv2

face_capture = cv2.CascadeClassifier("")

video_capture = cv2.VideoCapture(0)

while True:
    ret, video_data = video_capture.read()
    cv2.imshow("video live", video_data)
    if cv2.waitKey(10) == ord("a"):
        break
video_capture.release()