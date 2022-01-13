# -*- coding: utf-8 -*-

import string
import warnings as w
import TestFile as t
from random import randint, choice
from tkinter import *

CONST_LOGO = "password.png";
CONST_ICONE = "ico_copyshare.ico";

# test des images
if t.checkFileExist(CONST_LOGO) == False:
    w.warn('Le logo n\' existe pas ')
    exit()
if t.checkFileExist(CONST_ICONE) == False:
    w.warn('L\'icône n\' existe pas ')
    exit()


def generate_password():
    password_min = 8
    password_max = 12

    all_chars = string.ascii_letters + string.punctuation + string.digits
    # valeur table ascii (a-z) + ponctuation + chiffre

    pass_generate = ""
    for i in range(randint(password_min, password_max)):
        pass_generate = pass_generate + choice(all_chars)

    # on vide le champ puis on rajoute le pass generer
    champ_password.delete(0, END)
    champ_password.insert(0, pass_generate)


# =============================================================================
#     autre methode
#     generate = "".join(choise(all_chars)) for i in range(randint(password_min,password_max))
#        
# =============================================================================

taille_fenetre = "980x720"
couleur_bg = "#3c95ff"

# creation de la fenetre
window = Tk()
window.title("Generateur de mot de passe")
window.geometry(taille_fenetre)  # taille de la fentre
window.minsize(250, 250)  # taille minimum de la fenetre
window.config(backgroun=couleur_bg)  # change couleur de fond
window.iconbitmap(CONST_ICONE)

# frame principal
frame_principal = Frame(window, bg=couleur_bg)

# creation image
width = 300
height = 300
image = PhotoImage(file=CONST_LOGO).zoom(15).subsample(30)  # importation de l'image
canvas = Canvas(frame_principal, width=width, height=height, bg=couleur_bg, bd=0,
                highlightthickness=0)  # pour les composants graphique
canvas.create_image(width / 2, height / 2, image=image)  # position du canvas sur l'interface
#
canvas.grid(row=0, column=0, sticky=W)  # grid = tableau  sticky par rapport position dans la colonne

# sous boite
right_frame = Frame(frame_principal, bg=couleur_bg)

# titre dans la sous boite
label_title = Label(right_frame, text="Mot de passe", font=("Helvetica", 15), bg=couleur_bg, fg="white")
label_title.pack()  # mise en place label dans interface

# champs de saisie 2
champ_password = Entry(right_frame, text="Mot de passe", font=("Helvetica", 15), bg=couleur_bg, fg="white")
champ_password.pack()  # mise en place label dans interface

# champs de saisie
# =============================================================================
# conf_password = Entry(right_frame,text="Confirmation Mot de passe",font=("Helvetica",15), bg=couleur_bg, fg="white")
# conf_password.pack(pady=30) # mise en place label dans interface
# =============================================================================

# bouton password
bouton_valider = Button(right_frame, text="Génénrer", font=("Helvetica", 15), bg="white", fg="black",
                        command=generate_password)
bouton_valider.pack(pady=15, fill=X)  # mise en place label dans interface

# modelisation de la boite à droite
right_frame.grid(row=0, column=1, sticky=W)

# affichage frame
frame_principal.pack(expand=YES)

# creation d'une barre de menu
menu_barre = Menu(window)

# premier menu
first_menu = Menu(menu_barre, tearoff=0)
first_menu.add_command(label="Génénrer", command=generate_password)
first_menu.add_command(label="Quitter", command=window.destroy)

menu_barre.add_cascade(label="Fichier", menu=first_menu)  # ajout sous menu de fichier : nom menu et menu à rajouter

# configurer fenetre pour afficher menu barre
window.config(menu=menu_barre)

# affichage
window.mainloop()
