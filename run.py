import cv2
import mediapipe as mp
import serial
import time

# New
# Create an arduino connection object 
# 115200 Baud rate
ard = serial.Serial("/dev/ttyACM0", 115200)
DIRECTION = "S"

# Threshold values for the sensitivity of the model
# These are manually tuned
FROWARD_THRESHOLD = 0.1
LEFT_THRESHOLD = 0
RIGHT_THRESHOLD = 0.18

# Video capture object
cap = cv2.VideoCapture(0)


def classify_gesture(landmarks):
  # Thumb tip and MCP
  thumb_tip = landmarks[4]
  thumb_mcp = landmarks[2]

  # Index fingertip and MCP
  index_tip = landmarks[8]
  index_mcp = landmarks[5]

  # Determine gesture
  # Check orientation for open palm
  # print(thumb_tip.x - index_tip.x)

  if (thumb_tip.x - index_tip.x) < LEFT_THRESHOLD:
    return "L"
  elif (thumb_tip.x - index_tip.x) > RIGHT_THRESHOLD:
    return "R"
  elif (thumb_tip.x - index_tip.x) > FROWARD_THRESHOLD:
    return "F"
  else:
    return "S"

def run():
  # Hand detection models and hand landmark objects
  mpHands = mp.solutions.hands
  hands = mpHands.Hands()
  mpDraw = mp.solutions.drawing_utils

  # Classification
  global DIRECTION
  while True:
    sucess, img = cap.read()

    # Convert image to RGB
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    # print(results.multi_hand_landmarks)

    # Check for multiple hands and only keep one
    if results.multi_hand_landmarks:
      for handLms in results.multi_hand_landmarks:
        mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
        gesture = classify_gesture(handLms.landmark)

        if gesture != DIRECTION:
          print(gesture)
          # Send to arduino
          ard.write(gesture.encode("utf-8"))
        
        cv2.imshow("Live Video Feed", img)
        cv2.waitKey(1)

if __name__=="__main__":
  run()