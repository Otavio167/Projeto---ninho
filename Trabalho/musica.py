class Musica:
    def __init__(self, artista, nome, estilo, duracao, file):
        self.artista = artista
        self.nome = nome
        self.estilo = estilo
        self.duracao = duracao
        self.file = file

    def mostrar(self):
        print(f'''Artista: {self.artista}.
Nome: {self.nome}.
Estilo: {self.estilo}.
Duração: {self.duracao}.''')

# Lista de músicas
musicas = [
    Musica("Anitta", "Eu vou ficar!", "Funk", 149, 'Trabalho/rep_musicas/anita.wav'),
    Musica("Natanzinho", "Anjo Azul", "Sertanejo", 143, "Trabalho/rep_musicas/anjo.mp3"),
    Musica("Marilia Mendonça", "Troco de calçada", "Sertanejo", 154, "Trabalho/rep_musicas/mm.mp3"),
    Musica("Taty Pink", "Rotina", "Sertanejo", 167, "Trabalho/rep_musicas/rotina.mp3"),
    Musica("MC Brinquedo", "Medley", "Funk", 250, "Trabalho/rep_musicas/mcbri.mp3"),
    Musica("Anitta", "Sunshine", "Hip Hop", 230, "Trabalho/rep_musicas/delacruz.mp3")
]