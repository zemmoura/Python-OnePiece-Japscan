import requests
import os
from bs4 import BeautifulSoup
import urllib.request
import shutil
import subprocess
import os
import sys


def img_dl(path):

	## S	et up the image URL and filename
	image_url = path
	filename = image_url.split("/")[-1]

	# Open the url image, set stream to True, this will return the stream content.
	r = requests.get(image_url, stream = True)

	# Check if the image was retrieved successfully
	if r.status_code == 200:
	    # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
	    r.raw.decode_content = True
	    
	    # Open a local file with wb ( write binary ) permission.
	    with open(filename,'wb') as f:
	        shutil.copyfileobj(r.raw, f)
	        
	    print('Image sucessfully Downloaded: ',filename)
	    subprocess.call(["mv",filename,dir])
	else:
	    print('Image Couldn\'t be retreived')




#Recuperer le numero de chapitre a telecharger
chapitre = sys.argv[1]

dir="/home/abdelhakim/Bureau/One-Piece/chapitre/" + chapitre
subprocess.call(["mkdir", dir])

"""
print("Combien de page ?")
nbr = input()
"""
nbr = "17"

#Recuperer l'url de la page 1 du chapitre
url = "https://lelscan.net/scan-one-piece/" + chapitre


#Recuperer le code source de la page
page = requests.get(url)
status = page.status_code

for i in range (0,int(nbr)):
	soup = BeautifulSoup(page.text, 'html.parser') #On démarre le parser html
	img= soup.find('img')
	src=img.get("src")
	source="https://lelscan.net" + src
	image_source=source.split("jpg")
	url_final=image_source[0] + "jpg"
	img_dl(url_final)
	print(i)
	urlnouveau = url + "/" + str(i)
	print(urlnouveau)
	page = requests.get(urlnouveau)
	status = page.status_code
	print(status)
"""
image=dir+"/*.jpg"
nom_fichier = '*.jpg'
pdf= chapitre+".pdf"
os.chdir(dir)
subprocess.call(["ls", "-l"])
#subprocess.call(["img2pdf", "*" , "-o", pdf])

#subprocess.call(["cd","image/"])
#subprocess.Popen(["img2pdf","*.jpg","-o",pdf],cwd = dir)
"""