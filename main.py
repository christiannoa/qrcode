# install all the libraries needed
# create a function
# run the function
# save the qqr code as an image

# Import Library
import qrcode

# Creating an instance of QRCode class
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=3,
)

# Generate QR Code
qr.add_data("https://www.christiannoa.com/")
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
img.save("mainqrcn.png")
