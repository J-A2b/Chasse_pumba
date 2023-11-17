import pygame
import sys
import random
import time
import os
import ctypes
import pkg_resources
import io

# taille console
os.system('mode con: cols=33 lines=14')

hwnd = ctypes.windll.kernel32.GetConsoleWindow()
ctypes.windll.user32.SetWindowPos(hwnd, -1,4, 100, 50, 2, 0x0001)

# ___________
# Variables  \_
#              \
    # Taille de l'écran
largeur, hauteur = 700, 500
    # Taille d'une image
taille_case = 90
    # Vitesse curseur
vitesse = 16
    # valeur initiale du score
score = 0
    # pour le calcul des fps
horloge = pygame.time.Clock()
    # marge d erreur collision
marge = 7
marge2 = 7
    # taille balles
taille_balle = 20
    # evite erreur
temps_debut=time.time()
    #  nb de tir
nb_balles=0

# ____________/

#bank color
class Colors:
    RESET = '\033[0m'
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'

# __________________________
# Initialisation de Pygame  \__
#                              \
pygame.init()
    # Création de la fenêtre
ecran = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("tue le plus de sanglier en une minute!!!")
    # Chargez les images en utilisant pkg_resources (le binaire des fichiers)
image_zero_data = pkg_resources.resource_string(__name__, 'zero.png')
image_croix_data = pkg_resources.resource_string(__name__, 'croix.png')
image_fond_data = pkg_resources.resource_string(__name__, 'fond_ecran.jpg')
image_balle_data = pkg_resources.resource_string(__name__, 'balle.png')
    # Redimensionnez les images en exploitant le binaire
image_zero = pygame.transform.scale(pygame.image.load(io.BytesIO(image_zero_data)), (taille_case, taille_case))
image_croix = pygame.transform.scale(pygame.image.load(io.BytesIO(image_croix_data)), (taille_case, taille_case))
fond_ecran = pygame.transform.scale(pygame.image.load(io.BytesIO(image_fond_data)), (largeur, hauteur))
image_balle = pygame.transform.scale(pygame.image.load(io.BytesIO(image_balle_data)), (taille_balle, taille_balle))
    #positions initiales
x_croix, y_croix = random.randint(0, largeur - taille_case), random.randint(0, hauteur - taille_case)
x, y = largeur // 2, hauteur // 2
x_balle,y_balle=x,y
# _____________________/

# ----
# efface la console
os.system('cls' if os.name == 'nt' else 'clear')
# ----
# page de début
print(Colors.YELLOW+"_________________________________")
print("   bienvenue sur: CHASSE_PUMBA    ")
print("_________________________________"+Colors.RESET)
print("     ")
print(Colors.GREEN+"   les regles sont simples:")
print("   déplace toi avec z,q,s,d")
print("   appui sur ,m, pour tirer."+Colors.RESET)
print("  ")


# _-_-_-_-_-_-_-_-_-_-_-_-_-__
#   BOUCLE PRINCIPALE   --- __-_-
# _-_-_-_-_-_-_-_-_-_-_-_-_-_-
while True:

    # fermeture de tout si le jeu est quitté
    for evenement in pygame.event.get():
        if evenement.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Gestion des collisions et de l'augmentation du score
        if(x_croix <= x <= x_croix + taille_case-marge and
          y_croix <= y <= y_croix + taille_case-marge) or \
          (x <= x_croix <= x + taille_case and
          y <= y_croix <= y + taille_case):
            if evenement.type == pygame.KEYDOWN and evenement.key == pygame.K_m:
                score += 1
                x_croix, y_croix = random.randint(0, largeur - taille_case), random.randint(0, hauteur - taille_case)
        if evenement.type == pygame.KEYDOWN and evenement.key == pygame.K_m:
            x_balle, y_balle = x+43,y+43
            nb_balles=nb_balles+1

    temps_fin = time.time()
    duree = round(temps_fin - temps_debut)

    if duree > 60:
        pygame.quit()
        temps_fin = time.time()
        duree = round(temps_fin - temps_debut)
        # ----
        # efface la console
        os.system('cls' if os.name == 'nt' else 'clear')
        # ----
        print(Colors.CYAN+"_________________________________")
        print("ton score est: ", score)
        print("nombre de tir",nb_balles)
        print("_________________________________")
        input(Colors.RED+"appuie sur entré pour quitter")
        SystemExit

    # Gestion des déplacements du "0" --> chasseur
    touches = pygame.key.get_pressed()
    if touches[pygame.K_q] and x > vitesse:
        x -= vitesse
    if touches[pygame.K_d] and x < largeur - vitesse:
        x += vitesse
    if touches[pygame.K_z] and y > 0:
        y -= vitesse
    if touches[pygame.K_s] and y < hauteur - vitesse:
        y += vitesse
            
    # Effacer l'écran
    ecran.fill((255, 255, 255))

    # Dessiner le fond d'écran à l'arrière-plan
    ecran.blit(fond_ecran, (0, 0))
    # # Dessiner les "x" à leurs positions actuelles
    ecran.blit(image_croix, (x_croix, y_croix))
    # # Dessiner le "0" à la position actuelle
    ecran.blit(image_zero, (x, y))
    # dessiner la balle
    ecran.blit(image_balle, (x_balle,y_balle))

    # Mettre à jour l'écran
    pygame.display.flip()

    # Limiter le nombre d'images par seconde
    horloge.tick(30)










