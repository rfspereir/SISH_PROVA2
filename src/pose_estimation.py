import cv2
import cv2.aruco as aruco
import numpy as np

# Carregar parâmetros da calibração
data = np.load('../outputs/calibration_data.npz')
camera_matrix = data['camera_matrix']
dist_coeffs = data['dist_coeffs']

# Parâmetros do ArUco
aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_6X6_250)
parameters = aruco.DetectorParameters()

# Tamanho real do marcador (em metros)
marker_length = 0.05  # 5 cm

# Abrir câmera
cap = cv2.VideoCapture(0)  # Substituir pelo índice correto se usar DroidCam

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    corners, ids, _ = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)

    if ids is not None:
        rvec, tvec, _ = aruco.estimatePoseSingleMarkers(corners, marker_length, camera_matrix, dist_coeffs)

        aruco.drawDetectedMarkers(frame, corners, ids)

        for i in range(len(ids)):
            aruco.drawAxis(frame, camera_matrix, dist_coeffs, rvec[i], tvec[i], 0.03)
            print(f"ID {ids[i]} -> Posição (tvec): {tvec[i].flatten()} | Rotação (rvec): {rvec[i].flatten()}")

    cv2.imshow('Pose Estimation', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
