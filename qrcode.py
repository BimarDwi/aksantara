import cv2

def decode_qr_code(image):
    img = cv2.imread(image)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    data = cv2.QRCodeDetector().detectAndDecode(gray)
    if data:
        print("QR Code detected, data: ", data[0])
    else:
        print("QR Code not detected")

decode_qr_code("qrcode.png")
