import pygame

pygame.init()
pygame.mixer.music.load('C:\\Users\\STHEFANE\\Documents\\Prog Maquiavel cusos\\Python 1\\exercicios\\musica.mp3')
pygame.mixer.music.set_volume(1.0)
pygame.mixer.music.play()
input()
pygame.event.wait