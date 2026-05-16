
from pygame.mixer import Sound
from settings import *
from random import choice
import pygame.mixer
pygame.mixer.init()
#завантаж звукм невірного та пропущеної клавіши
wrong_sound = Sound(sounds_path + WRONG_SOUND)
missed_sound = Sound(sounds_path + MISSED_SOUND)

def load_sounds():
    sounds = {}
    
    for key,file in KEYS.items():
        sound = Sound(sounds_path + file)
        sounds[key] = sound
    return sounds



