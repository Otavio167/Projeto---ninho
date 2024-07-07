import pygame

class musica():
    
    def __init__(self, artista, nome, estilo, duracao, file):
        
        self.artista = artista
        self.nome = nome
        self.estilo = estilo
        self.duracao = duracao
        self.file = file
        
    def mostrar(selfie):
        
        print(f'''Artista: {selfie.artista}.
Nome: {selfie.nome}.
Estilo: {selfie.estilo}.
duração: {selfie.duracao}.''')
        
m1 = musica("Anita", "Eu vou ficar!", "Funk", 149, 'Trabalho/rep_musicas/anita.wav')
m2 = musica("Natanzinho", "Anjo Azul", "Sertanejo", 143, "Trabalho/rep_musicas/anjo.mp3" )
m3 = musica("Marila Medonça","Troco de calçada", "Sertanejo", 154, "Trabalho/rep_musicas/mm.mp3" )
m4 = musica("Taty Pink", "Rotina", "Sertanejo", 167, "Trabalho/rep_musicas/rotina.mp3")
m5 = musica("MC brinquedo", "Medlay", "Funk", 250, "Trabalho/rep_musicas/mcbri.mp3")
m6 = musica("Anita", "Sunshine", "Hip Hop", 230, "Trabalho/rep_musicas/delacruz.mp3")

lista_musicas = [m1, m2, m3, m4, m5, m6]

musicas = lista_musicas




        
        
        
    
