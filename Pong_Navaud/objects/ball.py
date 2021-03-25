import pygame
from game_object import GameObject
from pygame import Rect, Surface, Vector2, draw, font

# Définition de la classe Ball
class Ball(GameObject):

    # Constructeur de la classe
    def __init__(self, pos=Vector2(0, 0)):
        # La position de la balle (Vecteur)
        self.pos = pos
        # La direction de la balle (Vecteur normalisé)
        self.dir = Vector2(0.2, 0.2)
        # La vitesse de déplacement de la balle
        self.speed = 0.2
        # Le rayon de la balle en pixel
        self.size = 5


    # Méthode d'initialisation de l'objet, à exécuter une fois au début
    def init(self, screen: Surface):
        self.screen = screen
        self.pos = Vector2(screen.get_width()/2, screen.get_height()/2)

    # Méthode de mise à jour de l'objet, à exécuter à chaque image
    def update(self):

        # Ici vous bougez la balle
        if self.pos.x <= 0 :
            self.dir.x = self.speed
        if self.pos.x >= self.screen.get_width():
            self.dir.x = -self.speed
        if self.pos.y <= 0:
            self.dir.y = self.speed
        if self.pos.y >= self.screen.get_height():
            self.dir.y = -self.speed
        # Après on la dessine
        self.pos += self.dir
     

        draw.circle(self.screen, (255, 255, 255), self.pos, self.size)

    # Renvoi un rectangle aux même dimensions et position que la balle
    def as_rect(self):
        return Rect(self.pos, (self.size, self.size))
