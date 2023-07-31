import cv2
import dlib
import playsound
from scipy.spatial import distance as dist
import numpy as np
import threading

alarme = "alarm.mp3"

alarme_tocando = False

def tocar_alarme():
    global alarme_tocando
    alarme_tocando = True
    playsound.playsound(alarme)
    alarme_tocando = False

def eye_aspect_ratio(eye):
    # Calcula a distância euclidiana entre os pontos verticais dos olhos
    A = dist.euclidean(eye[1], eye[5])
    B = dist.euclidean(eye[2], eye[4])

    # Calcula a distância euclidiana entre o ponto horizontal do olho
    C = dist.euclidean(eye[0], eye[3])

    # Calcula a razão de aspecto
    ear = (A + B) / (2.0 * C)
    return ear

cap = cv2.VideoCapture(0)

hog_face_detector = dlib.get_frontal_face_detector()
dlib_facelandmark = dlib.shape_predictor("BancoDeRostos\shape_predictor_68_face_landmarks.dat")

# Índices dos marcos faciais dos olhos esquerdo e direito
left_eye_indices = list(range(36, 42))
right_eye_indices = list(range(42, 48))

# Variáveis para controlar o tempo
closed_counter = 0
closed_threshold = 2 * 30  # 3 segundos (considerando 30 quadros por segundo)

while True:

    # Inicia a detecção das posições de ambos os olhos
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = hog_face_detector(gray)
    for face in faces:
        face_landmarks = dlib_facelandmark(gray, face)

        left_eye = []
        for i in left_eye_indices:
            x = face_landmarks.part(i).x
            y = face_landmarks.part(i).y
            left_eye.append((x, y))

        right_eye = []
        for i in right_eye_indices:
            x = face_landmarks.part(i).x
            y = face_landmarks.part(i).y
            right_eye.append((x, y))

        # Calcula a razão de aspecto para o olho esquerdo e direito
        left_ear = eye_aspect_ratio(left_eye)
        right_ear = eye_aspect_ratio(right_eye)

        # Desenha os contornos dos olhos no quadro
        cv2.polylines(frame, [np.array(left_eye)], True, (0, 255, 0), 1)
        cv2.polylines(frame, [np.array(right_eye)], True, (0, 255, 0), 1)

        # Verifica se a razão de aspecto do olho esquerdo ou direito é menor que um valor de limite, se sim toca o alarme
        if left_ear < 0.2 or right_ear < 0.2:
            closed_counter += 1
            if closed_counter > closed_threshold and not alarme_tocando:
                # Start the alarm sound in a separate thread
                alarm_thread = threading.Thread(target=tocar_alarme)
                alarm_thread.start()
        else:
            closed_counter = 0

    cv2.imshow("Eye Detection", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break

# Release the camera and destroy all windows
cap.release()
cv2.destroyAllWindows()
