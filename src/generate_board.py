import cv2
import cv2.aruco as aruco
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import os

# Definir o dicionário ArUco
aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_6X6_250)

# Definir a placa (grid de marcadores)
board = aruco.GridBoard(
    size=(5, 7),  # 5 linhas e 7 colunas
    markerLength=0.04,  # Comprimento do lado do marcador em metros
    markerSeparation=0.01,  # Separação entre os marcadores em metros
    dictionary=aruco_dict
)

# Gerar a imagem da placa
img = board.generateImage((1000, 1000))

#cria diretório se não existir
output_dir = os.path.join(os.path.dirname(__file__), "..", "markers")
os.makedirs(output_dir, exist_ok=True)

# Salvar como PNG
cv2.imwrite(os.path.join(output_dir, "aruco_board.png"), img)

# Salvar como PDF
with PdfPages(os.path.join(output_dir, "aruco_board.pdf")) as pdf:
    plt.figure(figsize=(8.27, 11.69))  # A4
    plt.imshow(img, cmap='gray')
    plt.axis('off')
    plt.title('Placa ArUco 5x7')
    pdf.savefig(bbox_inches='tight')
    plt.close()