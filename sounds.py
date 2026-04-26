'''Звуки – завантаження та відтворення аудіо'''
from pygame.mixer import Sound
from settings import KEYS, WRONG_SOUND, MISSED_SOUND
from random import choice
import pygame.mixer
pygame.mixer.init()
path_file = "play_piano/assets/sounds/"
wong_sound = Sound(path_file + WRONG_SOUND)
missed_sound = Sound(path_file +MISSED_SOUND)
def load_sounds():
    sounds = {}
    
    for key,file in KEYS.items():
        sound = Sound(path_file + file)
        sounds[key] = sound
    return sounds

def load_rand_sounds():
    sounds = {}
    num = [1,2,3,4,5,6,7]
    path_file = "play_piano/assets/sounds/rand_sounds/"
    for key,file in KEYS.items():
        n = choice(num)
        num.remove(n)
        sound = Sound(path_file + f"rand_0{n}.wav")
        sounds[key] = sound
    return sounds
# 5. Створити функцію що завантажує звуки:

