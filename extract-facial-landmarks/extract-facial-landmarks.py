from cv2 import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(r'data/sample-video.mp4')
pTime = 0

mpDraw = mp.solutions.drawing_utils
mpFaceMesh = mp.solutions.face_mesh
faceMesh = mpFaceMesh.FaceMesh(max_num_faces=1)
drawSpec = mpDraw.DrawingSpec(thickness=2, circle_radius=3, color=(0, 255, 0))

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = faceMesh.process(imgRGB)

    if results.multi_face_landmarks:
        for face_landmark in results.multi_face_landmarks:
            mpDraw.draw_landmarks(img, face_landmark, mpFaceMesh.FACEMESH_CONTOURS, drawSpec, drawSpec)

    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime
    cv2.putText(img, f"FPS: {int(fps)}", (20, 70), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 255, 0), 3)
    cv2.imshow('Image', img)
    cv2.waitKey(1)
