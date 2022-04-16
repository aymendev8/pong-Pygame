import pygame

class t_balle :
    def __init__(self,ecran):
        self.ecran = ecran
        self.vitesse_en_x = 6
        self.vitesse_en_y = 6
        self.balle = pygame.rect.Rect(375,275,25,25)
    
    def dessiner_balle(self):
        pygame.draw.ellipse(self.ecran,(255,255,255),self.balle,2)
    
    def deplacement_balle(self):
        self.balle.x += self.vitesse_en_x 
        self.balle.y += self.vitesse_en_y 

    def delimitation_map(self):
        if self.balle.top <= 0 or self.balle.bottom >= 600:
            self.vitesse_en_y *= -1
        if self.balle.left <= 0 or self.balle.right >= 800:
            self.vitesse_en_x *= -1
    
    def balle_au_centre(self):
        self.balle.x = 400
        self.balle.y = 300

    def gagnant(self,ligne):
        if self.balle.colliderect(ligne):
            self.balle_au_centre()
            return True

    def colision_joueur(self,joueur1,joueur2):
        if self.balle.colliderect(joueur1) or self.balle.colliderect(joueur2):
            self.vitesse_en_x *= -1
    