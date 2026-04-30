
from pygame.mixer import Sound
from settings import *
from random import choice
import pygame.mixer
pygame.mixer.init()
#завантаж звукм невірного та пропущеної клавіши
wong_sound 
missed_sound 

def load_sounds():
    sounds = {}
    
    for key,file in KEYS.items():
        sound = Sound(sounds_path + file)
        sounds[key] = sound
    return sounds



