from ultralytics import YOLO
import cv2
import cvzone #to display detections

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720) #height
#cap = cv2.VideoCapture("../Videos/bikes.mp4")
# for video


model = YOLO("../Yolo-Weights/yolov8n.pt")

while True:
    succcess, img = cap.read()
    results = model(img, stream = True)
    for r in results:
        boxes = r.boxes
        for box in boxes:
            x1, y1, x2, y2 = box.xyxy[0] #easyer
            x1_y1_x2_y2 = int(x1), int(y1), int(x2), int(y2)
            print(x1, y1, x2, y2)
            x1, y1, x2, y2 = map(int, [x1, y1, x2, y2])
            cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
#turns camera on

