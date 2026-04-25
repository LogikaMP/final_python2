'''Звуки – завантаження та відтворення аудіо'''
from pygame.mixer import Sound
from settings import KEYS
from random import choice

def load_sounds():
    sounds = {}
    path_file = "assets/sounds/"
    for key,file in KEYS.items():
        sound = Sound(path_file + file)
        sounds[key] = sound
    return sounds


# 5. Створити функцію що завантажує звуки:

