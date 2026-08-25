import subprocess
import webbrowser
import pyautogui
import time
import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)


def get_finger_status(hand_landmarks):
    landmarks = hand_landmarks.landmark
    fingers = []

    if landmarks[4].x < landmarks[3].x:
        fingers.append(1)
    else:
        fingers.append(0)

    fingers.append(1 if landmarks[8].y < landmarks[6].y else 0)
    fingers.append(1 if landmarks[12].y < landmarks[10].y else 0)
    fingers.append(1 if landmarks[16].y < landmarks[14].y else 0)
    fingers.append(1 if landmarks[20].y < landmarks[18].y else 0)

    return fingers


def recognize_gesture(fingers):
    if fingers == [0, 0, 0, 0, 0]:
        return "FIST"
    elif fingers == [1, 1, 1, 1, 1]:
        return "OPEN PALM"
    elif fingers == [0, 1, 0, 0, 0]:
        return "ONE"
    elif fingers == [0, 1, 1, 0, 0]:
        return "PEACE"
    elif fingers == [0, 0, 1, 0, 0]:
        return "FUCK"
    elif fingers == [0, 1, 1, 1, 0]:
        return "THREE"
    elif fingers == [0, 1, 1, 1, 1]:
        return "FOUR"
    elif fingers == [1, 0, 0, 0, 0]:
        return "THUMBS UP"
    elif fingers == [0, 0, 0, 0, 1]:
        return "LITTLE"
    elif fingers == [1, 0, 0, 0, 1]:
        return "KICK"
    elif fingers == [0, 1, 0, 0, 1]:
        return "SWAG"
    else:
        return "UNKNOWN"


cap = cv2.VideoCapture(0)
screen_width, screen_height = pyautogui.size()
control_mode = False
previous_gesture = ""

while True:
    success, frame = cap.read()
    if not success:
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)
    gesture = ""

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            fingers = get_finger_status(hand_landmarks)
            gesture = recognize_gesture(fingers)

            if gesture != previous_gesture:
                if gesture == "THUMBS UP" and not control_mode:
                    webbrowser.open("https://www.google.com")
                    control_mode = True
                    previous_gesture = gesture
                elif gesture == "OPEN PALM" and not control_mode:
                    webbrowser.open("https://www.youtube.com")
                    control_mode = True
                    previous_gesture = gesture
                elif gesture == "ONE" and not control_mode:
                    subprocess.Popen("notepad.exe")
                    control_mode = True
                    previous_gesture = gesture
                elif gesture == "THREE" and not control_mode:
                    subprocess.Popen("calc.exe")
                    control_mode = True
                    previous_gesture = gesture
                elif gesture == "FOUR" and not control_mode:
                    subprocess.Popen("explorer.exe")
                    control_mode = True
                    previous_gesture = gesture
                elif gesture == "SWAG" and not control_mode:
                    pyautogui.hotkey("alt", "left")
                    control_mode = True
                    previous_gesture = gesture
                elif gesture == "KICK" and not control_mode:
                    pyautogui.hotkey("alt", "f4")
                    control_mode = True
                    previous_gesture = gesture
                elif gesture == "FUCK" and not control_mode:
                    pyautogui.hotkey("win", "d")
                    control_mode = True
                    previous_gesture = gesture

                if gesture == "LITTLE" and control_mode:
                    control_mode = False
                    print("Control Mode OFF")
                    previous_gesture = gesture

        cv2.putText(frame, f"Gesture : {gesture}", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Hand Gesture Recognition", frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
