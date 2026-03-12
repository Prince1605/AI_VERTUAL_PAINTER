import cv2
import numpy as np
from .ui import PALETTE

BRUSH_THICK = 12
ERASER_THICK = 60

def create_canvas(W, H):
    return np.zeros((H, W, 3), dtype=np.uint8)

def draw_line(canvas, pt1, pt2, color_idx):
    color = PALETTE[color_idx][1]
    thick = ERASER_THICK if PALETTE[color_idx][0].lower() == "eraser" else BRUSH_THICK
    cv2.line(canvas, pt1, pt2, color, thick, lineType=cv2.LINE_AA)

def merge_canvas(frame, canvas):
    gray = cv2.cvtColor(canvas, cv2.COLOR_BGR2GRAY)
    _, inv = cv2.threshold(gray, 20, 255, cv2.THRESH_BINARY_INV)
    inv = cv2.cvtColor(inv, cv2.COLOR_GRAY2BGR)
    base = cv2.bitwise_and(frame, inv)
    out = cv2.bitwise_or(base, canvas)
    return out
