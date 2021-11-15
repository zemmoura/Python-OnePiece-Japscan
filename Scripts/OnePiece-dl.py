#import librairy
import requests
from bs4 import BeautifulSoup
import shutil # to save it locally
import subprocess


def __download__(url, path):
    ## Set up the image URL and filename
    image_url = url
    filename = image_url.split("/")[-1]

    # Open the url image, set stream to True, this will return the stream content.
    r = requests.get(image_url, stream = True)

    # Check if the image was retrieved successfully
    if r.status_code == 200:
        # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
        r.raw.decode_content = True
        

        fichier = path + "/" + filename

        # Open a local file with wb ( write binary ) permission.
        with open(filename,'wb') as f:
            shutil.copyfileobj(r.raw, f)
            
        print('Image sucessfully Downloaded: ',filename)
    else:
        print('Image Couldn\'t be retreived')

    shutil.move(filename, fichier)
    print("move done")

    new_name = str(i) + ".jpg"

    subprocess.call(["cp",filename, new_name])

#construire l'url
base = "https://lelscans.net/scan-one-piece/"
chapitre = input("Quel chapitre ? \n")
pages = input("Nombre de page ?\n")
url= base + chapitre + "/" + pages
path =  "/home/abdelhakim/Bureau/One-Piece/test/"

for i in range (1,int(pages)+1):
    url= base + chapitre + "/" + str(i)
    requete = requests.get(url)
    soup = BeautifulSoup(requete.text,"html.parser")
    #print(soup)
    images = soup.findAll('img')
    image = images[0]
    #print (image['src'])
    src = image['src']
    img_rl = "https://lelscans.net" + src
    print (img_rl)
    __download__(img_rl,path)



nom_pdf = "One-Piece-" + chapitre + '.pdf'
*
subprocess.call(["img2pdf", "test/*.jpg", "-o", nom_pdf])