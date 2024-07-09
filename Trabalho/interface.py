import PySimpleGUI as sg
import os
from musica import Musica
from music_comands import get_files_inside_directory_not_recursive, play_sound, is_sound_playing, pause_sounds, stop_sounds, unpause

sg.theme('Reddit')

song_title_column = [
    [sg.Text(text='Pressione play...', justification='center', background_color='black', text_color='white', size=(200, 0), font='Tahoma', key='song_name')]
]

player_info = [
    [sg.Text('Player-Music', background_color='black', text_color='white', font=('Tahoma', 7))]
]

currently_playing = [
    [sg.Text(background_color='black', size=(200, 0), text_color='white', font=('Tahoma', 10), key='currently_playing')]
]

GO_BACK_IMAGE_PATH = 'Trabalho/Images/back.png'
GO_FORWARD_IMAGE_PATH = 'Trabalho/Images/next.png'
PLAY_SONG_IMAGE_PATH = 'Trabalho/Images/play_button.png'
PAUSE_SONG_IMAGE_PATH = 'Trabalho/Images/pause.png'
ALBUM_COVER_IMAGE_PATH = 'Trabalho/Images/pilot.png'

# Verifica se o caminho da imagem é válido
if not os.path.exists(ALBUM_COVER_IMAGE_PATH):
    print(f"Erro: Arquivo {ALBUM_COVER_IMAGE_PATH} não encontrado.")
else:
    main = [
        [sg.Canvas(background_color='black', size=(480, 20), pad=None)],
        [sg.Column(layout=player_info, justification='c', element_justification='c', background_color='black')],
        [
            sg.Canvas(background_color='black', size=(40, 350), pad=None),
            sg.Image(filename=ALBUM_COVER_IMAGE_PATH, size=(350, 350), pad=None),
            sg.Canvas(background_color='black', size=(40, 350), pad=None)
        ],
        [sg.Canvas(background_color='black', size=(480, 10), pad=None)],
        [sg.Column(song_title_column, background_color='black', justification='c', element_justification='c')],
        [sg.Text('_'*80, background_color='black', text_color='white')],
        [
            sg.Canvas(background_color='black', size=(99, 200), pad=(0, 0)),
            sg.Image(pad=(10, 0), filename=GO_BACK_IMAGE_PATH, enable_events=True, size=(35, 44), key='previous', background_color='black'),
            sg.Image(filename=PLAY_SONG_IMAGE_PATH, size=(64, 64), pad=(10, 0), enable_events=True, key='play', background_color='black'),
            sg.Image(filename=PAUSE_SONG_IMAGE_PATH, size=(58, 58), pad=(10, 0), enable_events=True, key='pause', background_color='black'),
            sg.Image(filename=GO_FORWARD_IMAGE_PATH, enable_events=True, size=(35, 44), pad=(10, 0), key='next', background_color='black'),
        ],
        [sg.Column(layout=currently_playing, justification='c', element_justification='c', background_color='black', pad=None)]
    ]

    window = sg.Window('Spoti-Ninho', layout=main, size=(480, 730), background_color='black', finalize=True, grab_anywhere=True, resizable=False)

    directory = sg.popup_get_folder('Select Music Directory')

    # Obtém as músicas do diretório e cria objetos Musica
    files_in_directory = get_files_inside_directory_not_recursive(directory)
    songs_in_directory = [Musica(artista='', nome=os.path.basename(file), estilo='', duracao=0, file=file) for file in files_in_directory]
    song_count = len(songs_in_directory)
    current_song_index = 0

    def update_song_display(window, musica):
        window['song_name'].update(musica.nome)
        window['currently_playing'].update(f'Tocando: {musica.nome} - {musica.artista}')

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == 'play':
            if not is_sound_playing():
                play_sound(songs_in_directory[current_song_index].file)
                update_song_display(window, songs_in_directory[current_song_index])

        elif event == 'pause':
            if is_sound_playing():
                pause_sounds()
            else:
                unpause()

        elif event == 'next':
            if current_song_index + 1 < song_count:
                stop_sounds()
                current_song_index += 1
                play_sound(songs_in_directory[current_song_index].file)
                update_song_display(window, songs_in_directory[current_song_index])
            else:
                print('Última música da lista')

        elif event == 'previous':
            if current_song_index > 0:
                stop_sounds()
                current_song_index -= 1
                play_sound(songs_in_directory[current_song_index].file)
                update_song_display(window, songs_in_directory[current_song_index])
            else:
                print('Primeira música da lista')

    window.close()