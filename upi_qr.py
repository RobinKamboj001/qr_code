import qrcode

# Function to generate QR Code
def generate_qr(data, filename="qrcode.png"):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill="black", back_color="white")
    img.save(filename)
    print(f"✅ QR Code saved as {filename}")

# Take user input
data = input("🔗 Enter text or URL to generate QR Code: ")
generate_qr(data)
