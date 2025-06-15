import cv2
import cv2.aruco as aruco
import matplotlib.pyplot as plt

# Definir o dicionário ArUco
aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_6X6_250)

# Definir a placa (grid de marcadores)
board = aruco.GridBoard_create(
    markersX=5,          
    markersY=7,          
    markerLength=0.04,   
    markerSeparation=0.01,  
    dictionary=aruco_dict
)

# Gerar a imagem da placa
img = board.draw(outSize=(1000, 1000))

# Salvar como PNG
cv2.imwrite("../markers/aruco_board.png", img)

# Visualizar antes de imprimir
plt.figure(figsize=(10, 10))
plt.imshow(img, cmap='gray')
plt.axis('off')
plt.title('Placa ArUco 5x7')
plt.show()
