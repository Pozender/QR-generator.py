import qrcode
import os
import shutil

#inputs
objectToEncode = input("Rentrez votre Url: ")
targetName = input("Entrez le nom de sortie du fichier: ")

#files format
PNG = targetName + ".png"

formats = [PNG]

#Qr personalisation
qr= qrcode.QRCode(
    version = 1,
    error_correction= qrcode.constants.ERROR_CORRECT_Q,
    box_size= 10,
    border= 6,
)

#setting of data in the code
qr.add_data(objectToEncode)
qr.make(fit=True)

#output custom
img = qr.make_image(fill_color= "black", back_color= "white")

#output file
try:
    os.mkdir(targetName)
except:
    folderexist = input("Ce fichier existe déjà veuillez le suprimmer, voulez vous le faire maintenant [Y/N]: ")
    if folderexist == "Y" or folderexist == "y":
        shutil.rmtree(targetName)
        print("nous venons de supprimer le dossier nous allons le recréer")
        os.mkdir(targetName)
    elif folderexist == "N" or folderexist == "n":
        print("Vous devez impérativement supprimer le dossier manuellement et relancer le programe pour le bon déroulement de celui-ci")
        breakpoint

for i in formats:
    
    #all create a file in a format of the list
    img.save(i)

    source = i
    target = targetName
    
    #copy the source in the target
    shutil.copy(source, target)

    #remove the source
    os.remove(source)
