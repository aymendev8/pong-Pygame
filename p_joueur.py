import pygame

class t_joueur :
    def __init__(self,x,y,ecran):
        self.x = x 
        self.y = y 
        self.ecran = ecran
        self.vitesse = 7
        self.couleur = (255,255,255)
        self.rectangle = pygame.rect.Rect(self.x,self.y,10,130)
        self.rectangle.x = self.x
        self.rectangle.y = self.y
    
    def dessiner_joueur(self):
        pygame.draw.rect(self.ecran,self.couleur,self.rectangle,2)

    def deplacement_haut(self):
        if self.rectangle.y > 0 :
            self.rectangle.y -= self.vitesse

    def deplacement_bas(self):
        if self.rectangle.y <= 475 :
            self.rectangle.y += self.vitesse
