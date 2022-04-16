import pygame
pygame.init()

class t_score : 
    def __init__(self,ecran):
         self.ecran = ecran
         self.score_joueur_1 = 0
         self.score_joueur_2 = 0
         self.score_max = 5
        
    def game_over(self):
        if self.score_joueur_1 or self.score_joueur_2 == self.score_max: 
            return True

    def afficher_score(self):
        police = pygame.font.SysFont("comicsans",20)
        score_j1 = police.render(str(self.score_joueur_1),1,(255,255,255))
        self.ecran.blit(score_j1,(200,20))
        score_j2 = police.render(str(self.score_joueur_2),1,(255,255,255))
        self.ecran.blit(score_j2,(600,20))

