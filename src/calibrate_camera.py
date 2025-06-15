import cv2
import cv2.aruco as aruco
import numpy as np
import glob
import os

# Definir parâmetros da placa
aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_6X6_250)
board = aruco.GridBoard_create(5, 7, 0.04, 0.01, aruco_dict)

# Listas para armazenar dados
all_corners = []
all_ids = []
image_size = None

# Carregar imagens
images = glob.glob('../calib/*.jpg')

if not images:
    print("Nenhuma imagem encontrada na pasta calib/.")
    exit()

for fname in images:
    img = cv2.imread(fname)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    image_size = gray.shape[::-1]

    corners, ids, _ = aruco.detectMarkers(gray, aruco_dict)

    if ids is not None:
        all_corners.append(corners)
        all_ids.append(ids)
        img = aruco.drawDetectedMarkers(img, corners, ids)
        cv2.imshow('Calibration', img)
        cv2.waitKey(500)

cv2.destroyAllWindows()

# Calibração
ret, camera_matrix, dist_coeffs, rvecs, tvecs = aruco.calibrateCameraAruco(
    all_corners, all_ids, board, image_size, None, None
)

print("Matriz Intrínseca (camera_matrix):\n", camera_matrix)
print("Coeficientes de Distorção (dist_coeffs):\n", dist_coeffs)

# Salvar parâmetros
if not os.path.exists('../outputs'):
    os.makedirs('../outputs')
np.savez('../outputs/calibration_data.npz', camera_matrix=camera_matrix, dist_coeffs=dist_coeffs)
