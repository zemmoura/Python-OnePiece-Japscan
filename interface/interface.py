from tkinter import *
import logging


logging.basicConfig(filename='Log_interf.log',
      format='%(asctime)s %(levelname)-8s %(message)s',
      level=logging.DEBUG,
      datefmt='%Y-%m-%d %H:%M:%S')



#Creer fct test
def appuie_bouton():
	logging.debug("Bouton Appuyé")
	text.set("reussi je crois")


#Creer fenetre
window = Tk()
logging.debug("Fenetre crée")

#Personalisation de la fenetre
window.title("One-Piece Downloader")
window.geometry("1080x720")
#window.iconbitmap("/home/abdelhakim/Bureau/One-Piece/logo.ico")
window.config(background='black')
logging.debug("Fenetre ajusté")

#Creation Frame
frame1= Frame(window,bg="black")
logging.debug("Creer frame1")

#Ajouter Consigne
label_consigne= Label(frame1,text="Quel chapitre télécharger ?", bg="black", fg="white")
label_consigne.pack()
#ajouter texte
label_titre = Label(window,text="OnePiece Downloader", background='black', font=("Courrier",25),fg='white')
label_titre.pack()

chapter = Entry(frame1,bg="grey")
chapter.pack(expand= YES)

submit_button = Button(frame1,text="Entrée",bg="white",fg="black", command=appuie_bouton)
submit_button.pack()
frame1.pack(expand= YES)
logging.debug("mise en page et ajout d'éléments")


text = StringVar()
text.set("Hello World!")
logging.debug("Creation de StringVar")

#Afficher fenetre
window.mainloop()
logging.debug("Fenetre fermé")


