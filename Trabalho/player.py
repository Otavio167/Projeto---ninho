import pygame
from musica import Musica

pygame.mixer.init()

class Player:
    def __init__(self):
        self.current_music = None

    def start(self, musica):
        self.current_music = musica
        pygame.mixer.music.load(musica.file)
        pygame.mixer.music.play()

    def pausar(self):
        pygame.mixer.music.pause()

    def despausar(self):
        pygame.mixer.music.unpause()

    def parar(self):
        pygame.mixer.music.stop()