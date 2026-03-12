import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.65,
    min_tracking_confidence=0.65
)

def get_landmarks(frame):
    """Returns landmarks list (x,y) or None"""
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    res = hands.process(rgb)
    lm = None
    if res.multi_hand_landmarks:
        h, w = frame.shape[:2]
        hand = res.multi_hand_landmarks[0]
        lm = [(int(pt.x * w), int(pt.y * h)) for pt in hand.landmark]
        mp_draw.draw_landmarks(frame, hand, mp_hands.HAND_CONNECTIONS)
    return lm, frame

def fingers_up(lm):
    """Detect index/middle finger up or not"""
    if lm is None:
        return {'index': False, 'middle': False}
    index_up = lm[8][1] < lm[6][1]
    middle_up = lm[12][1] < lm[10][1]
    return {'index': index_up, 'middle': middle_up}
