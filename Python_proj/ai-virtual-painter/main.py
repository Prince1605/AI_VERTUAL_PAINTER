import cv2
from utils import hand_tracker, painter, ui

W, H = 1280, 720
cap = cv2.VideoCapture(0)
cap.set(3, W)
cap.set(4, H)

canvas = painter.create_canvas(W, H)
current_color_idx = 0
prev_pt = None

while True:
    ok, frame = cap.read()
    if not ok: break
    frame = cv2.flip(frame, 1)

    boxes = ui.draw_palette(frame, current_color_idx)
    lm, frame = hand_tracker.get_landmarks(frame)
    state = hand_tracker.fingers_up(lm)

    if state['index'] and state['middle']:
        prev_pt = None
        if lm:
            idx_tip = lm[8]
            for i, box in enumerate(boxes):
                if ui.inside_box(idx_tip, box):
                    current_color_idx = i

    elif state['index'] and not state['middle']:
        if lm:
            idx_tip = lm[8]
            if prev_pt is not None:
                painter.draw_line(canvas, prev_pt, idx_tip, current_color_idx)
            prev_pt = idx_tip
    else:
        prev_pt = None

    out = painter.merge_canvas(frame, canvas)
    cv2.imshow("AI Virtual Painter", out)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'): break
    if key == ord('c'): canvas[:] = 0

cap.release()
cv2.destroyAllWindows()
