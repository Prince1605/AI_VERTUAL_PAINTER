import cv2

PALETTE = [
    ("Blue", (255, 0, 0)),
    ("Green", (0, 255, 0)),
    ("Red", (0, 0, 255)),
    ("Yellow", (0, 255, 255)),
    ("Purple", (255, 0, 255)),
    ("Eraser", (0, 0, 0)),
]

PALETTE_BOX_W = 180
PALETTE_BOX_H = 70
PALETTE_Y1 = 10
PALETTE_Y2 = PALETTE_Y1 + PALETTE_BOX_H
FONT = cv2.FONT_HERSHEY_SIMPLEX

def draw_palette(img, current_idx):
    boxes = []
    x1 = 10
    for i, (name, color) in enumerate(PALETTE):
        x2 = x1 + PALETTE_BOX_W
        thickness = -1 if i == current_idx else 2
        cv2.rectangle(img, (x1, PALETTE_Y1), (x2, PALETTE_Y2), color, thickness)
        cv2.putText(img, name, (x1+10, PALETTE_Y1+45), FONT, 0.8, (255,255,255), 2)
        boxes.append((x1, PALETTE_Y1, x2, PALETTE_Y2))
        x1 = x2 + 10
    return boxes

def inside_box(pt, box):
    x, y = pt
    x1, y1, x2, y2 = box
    return x1 <= x <= x2 and y1 <= y <= y2
