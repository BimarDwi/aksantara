import cv2

def decode_qr_code(image):
    # Read the image
    img = cv2.imread(image)

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Initialize the QR code detector
    qr_detector = cv2.QRCodeDetector()

    # Detect QR code in the image
    data = qr_detector.detectAndDecode(gray)

    if data[0]:
        print("QR Code detected, data: ", data[0])
    else:
        print("QR Code not detected")

# Example usage
decode_qr_code("qrcode.png")
