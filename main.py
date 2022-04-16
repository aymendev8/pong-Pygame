import pygame
import p_joueur
import p_balle
import p_score
import p_bouton

# mes variables 
mon_ecran_l = 800
mon_ecran_h = 600
mon_horloge = pygame.time.Clock()

# fenetre de jeu
pygame.init()
mon_ecran = pygame.display.set_mode((mon_ecran_l,mon_ecran_h))
pygame.display.set_caption("Pong - By Aymen")

#les joueurs - balles - score 
le_joueur_1 = p_joueur.t_joueur(20,255,mon_ecran)
le_joueur_2 = p_joueur.t_joueur(768,255,mon_ecran)
la_balle = p_balle.t_balle(mon_ecran)
le_score = p_score.t_score(mon_ecran)
# boucle du jeu 
jeu = True
parti_en_cours = False
while jeu : 

    mon_horloge.tick(60)
    if not parti_en_cours : 
        mon_ecran.blit(pygame.image.load("Images/fond.jpg"),(-700,-90))
        bouton_play = p_bouton.t_bouton(pygame.image.load("Images/bouton_jouer.png"),303,246)
        bouton_quit = p_bouton.t_bouton(pygame.image.load("Images/bouton_quitter.png"),303,346)
        bouton_play.dessiner_bouton(mon_ecran)
        bouton_quit.dessiner_bouton(mon_ecran)

    if parti_en_cours : 
        mon_ecran.fill((0,0,0))
        pygame.draw.line(mon_ecran,(255,255,255),(400,0),(400,600),1)
        a = pygame.draw.line(mon_ecran,(0,0,0),(799,0),(799,600),1)
        b = pygame.draw.line(mon_ecran,(0,0,0),(0,0),(0,600),1)
        #joueurs 
        le_joueur_1.dessiner_joueur()
        le_joueur_2.dessiner_joueur()
        #balle
        la_balle.dessiner_balle()
        la_balle.deplacement_balle()
        la_balle.delimitation_map()
        la_balle.colision_joueur(le_joueur_1.rectangle,le_joueur_2.rectangle)
        #score
        le_score.afficher_score()
        if la_balle.gagnant(a):
            le_score.score_joueur_1 += 1
        if la_balle.gagnant(b):
            le_score.score_joueur_2 += 1


    key = pygame.key.get_pressed()
    if key[pygame.K_z]:
        le_joueur_1.deplacement_haut()
    if key[pygame.K_s]:
        le_joueur_1.deplacement_bas()
    if key[pygame.K_UP]:
        le_joueur_2.deplacement_haut()
    if key[pygame.K_DOWN]: 
        le_joueur_2.deplacement_bas()

    for evt in pygame.event.get():
        if evt.type == pygame.QUIT:
            jeu = False
        if evt.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if bouton_play.est_cliquer(pos):
                parti_en_cours = True
            if bouton_quit.est_cliquer(pos):
                jeu = False                

    pygame.display.flip()
pygame.quit()

