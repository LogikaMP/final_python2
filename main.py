'''Main – запуск гри та обробка подій'''
# 6. Імпортуємо все що необхідно для роботи гри
import pygame
from settings import GRAY, WINDOW_WIDTH, WINDOW_HEIGHT, WHITE,GRAY,BLUE ,KEYS, FON, FON_SOUND
from keys import create_keys, draw_keys,load_sounds_img, move_keys, check_keys
from effects import draw_effect_sound
from sounds import load_sounds, load_rand_sounds, wong_sound, missed_sound
from random import randint
from buttons import Button
'''Додай імопрт класу меню'''

# 7. Ініцилізація та Створити вікно 
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
# 8. Створити список ректів - клавіш
btn_start = Button(20,20,100,40,GRAY,"Level 1",WHITE,BLUE,None)
# 9. Створити порожню множину - натиснуті клавіши
keys_pressed = set()
# 10. Створити список звуків - завантажити звуки нот
keys_sounds = load_sounds()
keys_rect = create_keys(7)
'''Створи обєкт меню:
координати - 20,20,
розмір - 100, 40
кольри - GREY, WHITE, BLUE'''

# 11. Головний цикл гри:
run = True
game_part = "start"
while run:
   
# - обробка закртиття вікна
   for event in pygame.event.get():
      '''виклич метод оновлення меню - передай подію event'''
      
        
      if event.type == pygame.QUIT:
         run = False

#  - обробка кліку по клавішам  
      if event.type == pygame.MOUSEBUTTONDOWN :
         pos = event.pos
         
         

#  - відобразити фон, клавіши, оновити вікно
   window.fill(FON)
   draw_keys(window,keys_rect,keys_pressed)
      

   pygame.display.flip()
   clock.tick(120)
    # обробка лкіку по клавішам


