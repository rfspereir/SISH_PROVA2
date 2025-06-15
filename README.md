# Pose Estimation QRCode com OpenCV e ArUco

Projeto para estimativa de posição e orientação de um robô utilizando câmera e QR Codes (marcadores ArUco).

## 🎯 Funcionalidades

- Calibração da câmera usando placas ArUco.
- Detecção de marcadores.
- Estimativa de posição (distância) e orientação (yaw, pitch, roll).
- Visualização em tempo real.

---

## 🛠️ Configuração do Ambiente

### ✅ Requisitos

- Python 3.8+
- Sistema operacional: Linux (testado em Arch Linux KDE6)
- Câmera: Webcam, DroidCam (Galaxy Note 10) ou ESP32 CAM

### 📦 Instalação

1. Clone o projeto:

```bash
git clone <seu-repositorio>
cd pose_estimation_qrcode
```

2. Crie um ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

---

## 🚀 Execução dos Scripts

### 🔸 Gerar Placa ArUco para Impressão

```bash
python src/generate_board.py
```
O arquivo será salvo em `/markers/aruco_board.png`.

---

### 🔸 Calibração da Câmera

1. Coloque a placa ArUco em diferentes ângulos e distâncias.
2. Capture de 10 a 20 imagens e salve na pasta `/calib`.

3. Execute:

```bash
python src/calibrate_camera.py
```

O arquivo `calibration_data.npz` será salvo na pasta `/outputs`.

---

### 🔸 Detecção de QR Code com Estimativa de Posição e Orientação

Execute:

```bash
python src/pose_estimation.py
```

A janela exibirá o feed da câmera com o marcador detectado, além dos eixos representando orientação.

---

## 🔗 Uso do Galaxy Note 10 como Câmera

### 🔸 Opção 1: DroidCam

1. Instale o app DroidCam no celular.
2. No Arch Linux:

```bash
sudo pacman -S v4l2loopback-dkms
yay -S droidcam
```

3. Execute o cliente DroidCam:

```bash
droidcam
```

4. A câmera aparecerá como `/dev/video2` (verifique com `v4l2-ctl --list-devices`).

No código Python:

```python
cap = cv2.VideoCapture(2)  # Substituir pelo ID correto
```

### 🔸 Opção 2: IP Webcam

- No app: iniciar o servidor → copie o link `http://<ip>:8080/video`
- No código Python:

```python
cap = cv2.VideoCapture("http://<ip>:8080/video")
```

---

## 📁 Estrutura Recomendada

```
pose_estimation_qrcode/
│
├── calib/                  # Imagens para calibração
├── markers/                # Placas ArUco geradas
├── src/                    # Códigos fonte
├── outputs/                # Arquivos de calibração
├── requirements.txt
└── README.md
```

---

## ✍️ Autor

- Rafael Pereira - Recuperação Engenharia
