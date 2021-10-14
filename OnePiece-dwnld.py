#import librairy
import requests
from bs4 import BeautifulSoup
import shutil # to save it locally



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


url = "https://lelscan-vf.co/uploads/manga/one-piece/chapters/1028/01.jpg"
path =  "/home/abdelhakim/Bureau/One-Piece/test"
#__download__(url,path)





#construire l'url
base = "https://lelscans.net/scan-one-piece/"
chapitre = input("Quel chapitre ? \n")
pages = input("Nombre de page ?\n")

"""
url= base + chapitre + "/" + pages
#print (url)


#scrapper image
requete = requests.get(url)
soup = BeautifulSoup(requete.text,"html.parser")
#print(soup)
images = soup.findAll('img')
image = images[0]
print (image['src'])

#https://lelscans.net/mangas/one-piece/1007/01.jpg?v=fr1615535358

#Download l'image
"""

path= "home/abdelhakim/Bureau/One-Piece/" + chapitre 

#iterer nombre de page
for i in range (1,int(pages)+1):
    url= base + chapitre + "/" + str(i)
    #print(url)
    __download__(url,path)
