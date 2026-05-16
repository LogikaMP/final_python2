'''Ефекти – анімація клавіш і візуальні ефекти'''
from pygame import image,transform, display
from settings import *
key_up = image.load("assets/images/key_pressed.png")
key_down = image.load("assets/images/key_unpressed.png")


def draw_effect(screen, rect, pressed):
    if pressed:
        img = key_up
    else:
        
        img = key_down
    img = transform.scale(img,(rect.w,rect.h))
    screen.blit(img,rect)
#додай функцію draw_start(), 
# яка буде відображати анімацію на стартовому екрані,
#  використовуючи список зображень для анімації та циклічно їх відображаючи
def draw_start(window,x, y):
    for i in range(200,900):
        img = image.load(images_path + f"start_{i//200}.png")
        img = transform.scale(img,(100,100))
        window.blit(img,(x,y))
        display.flip()