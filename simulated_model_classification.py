import cv2
import mediapipe as mp

DIRECTION = "stop"

# Threshold vales for the sensitivity of classification
# These are manually tuned
FROWARD_THRESHOLD = 0.1
LEFT_THRESHOLD = 0
RIGHT_THRESHOLD = 0.18

# Video capture object
cap = cv2.VideoCapture(0)

# Hand detection models and hand landmark objects
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils


# Classify gestures using landmarks
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
        return "left"
    elif (thumb_tip.x - index_tip.x) > RIGHT_THRESHOLD:
        return "right"
    elif (thumb_tip.x - index_tip.x) > FROWARD_THRESHOLD:
        return "forward"
    else:
        return "stop"


def get_direction():
    global DIRECTION
    try:
        while True:
            success, img = cap.read()

            # Converting image colours to RGB
            imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            results = hands.process(imgRGB)

            #print(results.multi_hand_landmarks)

            # Check for multiple hands
            # Extracting each hand
            if results.multi_hand_landmarks:
                for handLms in results.multi_hand_landmarks:
                    mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

                    # Calculate the bounding box
                    x_min, x_max = min([lm.x for lm in handLms.landmark]), max([lm.x for lm in handLms.landmark])
                    y_min, y_max = min([lm.y for lm in handLms.landmark]), max([lm.y for lm in handLms.landmark])
                    x_min, x_max, y_min, y_max = int(x_min * img.shape[1]), int(x_max * img.shape[1]), int(y_min * img.shape[0]), int(y_max * img.shape[0])

                    # Draw bounding box
                    cv2.rectangle(img, (x_min, y_min), (x_max, y_max), (255,0,0), 2)

                    # Classify gesture
                    gesture = classify_gesture(handLms.landmark)
                    cv2.putText(img, gesture, (x_min, y_min - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2)
                    if gesture != DIRECTION:
                        print(gesture)
                        DIRECTION = gesture

            cv2.imshow("Live Video Feed", img)
            cv2.waitKey(1)
    except KeyboardInterrupt:
        print("Process stopped")
    finally:
        print("OBJ terminated")


if __name__ == "__main__":
    get_direction()
