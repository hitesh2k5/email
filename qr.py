import qrcode

# URL of the local server (adjust if needed)
url = "http://127.0.0.1:5000/"

# Create a QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

# Create an image of the QR code
img = qr.make_image(fill='black', back_color='white')
img.save("qr_code.png")
