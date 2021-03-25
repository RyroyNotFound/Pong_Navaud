from pygame import key, Rect, Surface, Vector2, draw, Rect
from pygame.constants import K_DOWN, K_UP
from game_object import GameObject
from objects.ball import Ball

# Définition de la classe Paddle
class Paddle(GameObject):

    # Constructeur de la classe
    def __init__(self, ball: Ball = None, is_player=True):
        self.pos = Vector2(0,0)
        # Position de la raquette
        self.rect = Rect((self.pos.x,self.pos.y),(5,100))
        # La raquette est controlée par le joueur ? O/N
        self.is_player = is_player
        # Quelle est la balle du jeu (pour l'IA)
        self.ball = ball
        # Vitesse de déplacement de la raquette
        self.speed = 0.5

    # Méthode d'initialisation de l'objet, à exécuter une fois au début
    def init(self, screen: Surface):
        self.screen = screen

    # Méthode de mise à jour de l'objet, à exécuter à chaque image
    def update(self):
        # Il existe une fonction par type de joueur, manuel ou IA
        if (self.is_player):
            self.manual_control()
        else:
            self.automatic_control()

        # Maintenant que les coordonées ont changés, on dessine la raquette
        draw.rect(self.screen, (255, 255, 255), self.rect)

    def manual_control(self):

        # Ici vous mettez votre logique de mouvement, avec les touches de clavier etc.
        if key.get_pressed()[K_UP]:
            self.pos.y -=0.2
            if self.pos.y < 0:
                self.pos.y = 0
        if key.get_pressed()[K_DOWN]:
            self.pos.y +=0.2
            if self.pos.y > (self.screen.get_height()-50):
                self.pos.y = self.screen.get_height()-50
        
        self.rect = Rect((self.pos.x,self.pos.y),(5,100)) 
            

    # Imbattable, la raquette suis la balle directement sans faute
    def automatic_control(self):

        self.pos.x = self.screen.get_width() - 5
        self.pos.y = self.ball.pos.y - 50
        self.rect = Rect((self.pos.x,self.pos.y),(5,100)) 

    def as_rect(self):
        return self.rect
