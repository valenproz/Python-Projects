import qrcode

qr_data = 'www.linkedin.com'
qr_img = qrcode.make(qr_data)
save_path = 'Project4QRCodeGenerator\\' + qr_data + '.png'
qr_img.save(save_path)