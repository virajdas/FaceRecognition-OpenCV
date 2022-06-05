import cv2

cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
cam = cv2.VideoCapture(0)

while True:
    _, frame = cam.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = cascade.detectMultiScale(gray, 2, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 1)
        cv2.putText(frame, "I See You", (x, y - 10), 1, 1.5, (255, 255, 255), 2)

    cv2.imshow("I See You - Viraj", frame)

    key = cv2.waitKey(1)
    if key == ord("q"):
        break