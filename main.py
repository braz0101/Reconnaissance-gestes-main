import cv2
import mediapipe as mp
import math
import numpy as np
from PIL import ImageFont, ImageDraw, Image

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

def calculate_angle(a, b, c):
    ab = [a.x - b.x, a.y - b.y]
    cb = [c.x - b.x, c.y - b.y]
    dot_product = ab[0] * cb[0] + ab[1] * cb[1]
    magnitude_ab = math.hypot(*ab)
    magnitude_cb = math.hypot(*cb)
    if magnitude_ab * magnitude_cb == 0:
        return 0
    angle = math.acos(dot_product / (magnitude_ab * magnitude_cb))
    return math.degrees(angle)

def is_thumb_up(landmarks):
    thumb_angle = calculate_angle(landmarks[2], landmarks[3], landmarks[4])
    other_fingers_folded = all(landmarks[tip].y > landmarks[dip].y for tip, dip in [(8,6), (12,10), (16,14), (20,18)])
    return thumb_angle > 150 and other_fingers_folded

def is_palm_open(landmarks):
    return all(landmarks[tip].y < landmarks[dip].y for tip, dip in [(8,6), (12,10), (16,14), (20,18)])

def is_two_fingers_up(landmarks):
    return (landmarks[8].y < landmarks[6].y and
            landmarks[12].y < landmarks[10].y and
            landmarks[16].y > landmarks[14].y and
            landmarks[20].y > landmarks[18].y)

def is_fist_closed(landmarks):
    return all(landmarks[tip].y > landmarks[pip].y for tip, pip in [(8,6), (12,10), (16,14), (20,18)])

# Texte avec contour (ombre) pour meilleure lisibilité
def draw_text_with_outline(img, text, pos, font_path="arial.ttf", font_size=32, text_color=(0,255,0), outline_color=(0,0,0), outline_thickness=2):
    img_pil = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(img_pil)
    try:
        font = ImageFont.truetype(font_path, font_size)
    except:
        font = ImageFont.load_default()
    x, y = pos
    # contour (ombre)
    for dx in [-outline_thickness, 0, outline_thickness]:
        for dy in [-outline_thickness, 0, outline_thickness]:
            if dx != 0 or dy != 0:
                draw.text((x+dx, y+dy), text, font=font, fill=outline_color)
    # texte principal
    draw.text(pos, text, font=font, fill=text_color)
    return cv2.cvtColor(np.array(img_pil), cv2.COLOR_RGB2BGR)

def main():
    cap = cv2.VideoCapture(0)
    with mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7, min_tracking_confidence=0.7) as hands:
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            frame = cv2.flip(frame, 1)
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            result = hands.process(rgb)
            gesture = "Aucun geste"

            if result.multi_hand_landmarks:
                for hand_landmarks in result.multi_hand_landmarks:
                    # Landmarks avec épaisseur plus fine
                    mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS,
                                              mp_drawing.DrawingSpec(color=(0,255,0), thickness=1, circle_radius=3),
                                              mp_drawing.DrawingSpec(color=(0,128,0), thickness=1))
                    landmarks = hand_landmarks.landmark

                    if is_thumb_up(landmarks):
                        gesture = "Pouce levé"
                    elif is_palm_open(landmarks):
                        gesture = "Paume ouverte"
                    elif is_two_fingers_up(landmarks):
                        gesture = "Deux doigts levés"
                    elif is_fist_closed(landmarks):
                        gesture = "Poing fermé"
                    else:
                        gesture = "Main détectée"

            # Fond semi-transparent derrière le texte
            overlay = frame.copy()
            h, w, _ = frame.shape
            rect_x1, rect_y1 = 5, h - 55
            rect_x2, rect_y2 = 350, h - 5
            cv2.rectangle(overlay, (rect_x1, rect_y1), (rect_x2, rect_y2), (0,0,0), -1)
            alpha = 0.5
            frame = cv2.addWeighted(overlay, alpha, frame, 1 - alpha, 0)

            # Texte avec contour en bas à gauche
            frame = draw_text_with_outline(frame, f"Geste : {gesture}", (10, h - 45))

            cv2.imshow("Reconnaissance Gestes Main", frame)

            if cv2.waitKey(1) & 0xFF == 27:
                break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
