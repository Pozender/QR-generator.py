import qrcode

#inputs
objectToEncode = input("Rentrez votre Url: ")
targetName = input("Entrez le nom de sortie du fichier: ")

#files format
PNG = targetName + ".png"
SVG = targetName + ".svg"
JPG = targetName + ".jpg"

#Qr personalisation
qr= qrcode.QRCode(
    version = 1,
    error_correction= qrcode.constants.ERROR_CORRECT_Q,
    box_size= 5,
    border= 4,
)

#setting of data in the code
qr.add_data(objectToEncode)
qr.make(fit=True)

#output custom
img = qr.make_image(fill_color= "black", back_color= "white")

#output file
img.save(PNG)
img.save(SVG)
img.save(JPG)