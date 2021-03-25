from game_object import GameObject
from objects.paddle import Paddle
from pygame.surface import Surface
from objects.ball import Ball

# Une classe qui va gérer la logique du jeu


class Game(GameObject):
    # On crée nos objets
    ball = Ball()
    player_paddle = Paddle(ball, True)
    enemy_paddle = Paddle(ball, False)

    # Indique si la boucle de jeu doit tourner ou non
    should_run = True

    # Lance les init de chaque objet au démarrage du jeu
    def init(self, screen: Surface):
        self.ball.init(screen)
        self.player_paddle.init(screen)
        self.enemy_paddle.init(screen)

    # Lance les update de chaque objet à chaque frame et gère la
    # relation entre les objets
    def update(self):
        self.ball.update()
        self.player_paddle.update()
        self.enemy_paddle.update()

        # gestion de la collision entre ball et les paddles
        compteur = 0 
        if self.ball.pos.x <= 0:
            if self.ball.as_rect().colliderect(self.player_paddle.as_rect()) == False:
                self.should_run = False
 
    


                


