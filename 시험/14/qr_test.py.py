import qrcode

url = "https://github.com/parkhesu/openAPI.git"
img = qrcode.make(url)
img.save("qr_github.png")