import requests
import os
from bs4 import BeautifulSoup
import urllib.request
import shutil
import subprocess


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
	else:
	    print('Image Couldn\'t be retreived')




#Recuperer le numero de chapitre a telecharger
print("Quel chapitre telecharger ?")
chapitre = input()

print("Combien de page ?")
nbr = input()

#Recuperer l'url de la page 1 du chapitre
url = "https://www.japscan.se/manga/one-piece/" + chapitre


#Recuperer le code source de la page
page = requests.get(url)
status = page.status_code

for i in range (0,int(nbr)):
	soup = BeautifulSoup(page.text, 'html.parser') #On démarre le parser html
	img= soup.find('pages')
	src=img.get("img")
	print(src)
	#image_source=src.split("jpg")
	#url_final=image_source[0] + "jpg"
	img_dl(img)
	print(i)
	urlnouveau = url + "/" + str(i)
	print(urlnouveau)
	page = requests.get(urlnouveau)
	status = page.status_code
	print(status)
