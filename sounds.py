'''Звуки – завантаження та відтворення аудіо'''
from pygame.mixer import Sound
from settings import KEYS, KEYS_RAND
from random import choice

def load_sounds():
    sounds = {}
    path_file = "assets/sounds/"
    for key,file in KEYS.items():
        sound = Sound(path_file + file)
        sounds[key] = sound
    return sounds


# 5. Створити функцію що завантажує звуки:

'''НОВЕ: Створи функцію завантаження випадкових звуків load_rand_sound:
все так само як у функції load_sounds, лише використай
словник - KEYS_RAND 
шлях до папки зі звуками - "assets/sounds/rand_sounds/"'''
