import PySimpleGUI as sg
import os
import pygame
from musica import musicas
from player import Player
from music_comands import get_files_inside_directory_not_recursive

# Função para atualizar a exibição da música
def update_song_display(window, musica):
    window['song_name'].update(musica.nome)
    window['currently_playing'].update(f'Tocando: {musica.nome} - {musica.artista}')

# Layout da interface gráfica
layout = [
    [sg.Text(text='Pressione play..', justification='center', background_color='black', text_color='white', size=(200, 0), font='Tahoma', key='song_name')],
    [sg.Text('PySimpleGUI Player-Music', background_color='black', text_color='white', font=('Tahoma', 7))],
    [sg.Image(filename='Images/pylot.png', size=(350, 350))],
    [sg.Button('Anterior', key='previous'), sg.Button('Play', key='play'), sg.Button('Pausar', key='pause'), sg.Button('Próxima', key='next')],
    [sg.Text(background_color='black', size=(200, 0), text_color='white', font=('Tahoma', 10), key='currently_playing')]
]

# Criação da janela
window = sg.Window('Spotify', layout, size=(480, 730), background_color='black', finalize=True, grab_anywhere=True, resizable=False)

player = Player()
current_song_index = 0

# Loop principal
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'play':
        player.start(musicas[current_song_index])
        update_song_display(window, musicas[current_song_index])
    elif event == 'pause':
        if pygame.mixer.music.get_busy():
            player.pausar()
        else:
            player.despausar()
    elif event == 'next':
        if current_song_index + 1 < len(musicas):
            current_song_index += 1
            player.start(musicas[current_song_index])
            update_song_display(window, musicas[current_song_index])
    elif event == 'previous':
        if current_song_index > 0:
            current_song_index -= 1
            player.start(musicas[current_song_index])
            update_song_display(window, musicas[current_song_index])

window.close()