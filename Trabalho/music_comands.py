import os
from pygame import mixer

mixer.init()

def get_files_inside_directory_not_recursive(directory):
    files = [os.path.join(directory, file) for file in os.listdir(directory) if os.path.isfile(os.path.join(directory, file))]
    return files

def play_sound(sound_path):
    mixer.music.load(sound_path)
    mixer.music.play()

def stop_sounds():
    mixer.music.stop()

def pause_sounds():
    mixer.music.pause()

def unpause():
    mixer.music.unpause()

def is_sound_playing():
    return mixer.music.get_busy()