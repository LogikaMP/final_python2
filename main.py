'''Main – запуск гри та обробка подій'''
# 6. Імпортуємо все що необхідно для роботи гри
import pygame
from settings import GRAY, WINDOW_WIDTH, WINDOW_HEIGHT, WHITE,GRAY,BLUE ,KEYS, FON
from keys import create_keys, draw_keys
from effects import draw_effect_sound
from sounds import load_sounds
'''Додай імопрт класу меню'''
from ui.settingsUi import SettingsMenu
# 7. Ініцилізація та Створити вікно 
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
setting = SettingsMenu(20,20,100,40,GRAY,WHITE,BLUE)
# 8. Створити список ректів - клавіш
keys_rect = create_keys(setting.num_keys)

# 9. Створити порожню множину - натиснуті клавіши
keys_pressed = set()
# 10. Створити список звуків - завантажити звуки нот
keys_sounds = load_sounds()

'''Створи обєкт меню:
координати - 20,20,
розмір - 100, 40
кольри - GREY, WHITE, BLUE'''

# 11. Головний цикл гри:
run = True
while run:
   setting.update()
# - обробка закртиття вікна
   for event in pygame.event.get():
      '''виклич метод оновлення меню - передай подію event'''
      setting.update(event)
      if len (keys_rect) != setting.num_keys:
         keys_rect = create_keys(setting.num_keys)
        
      if event.type == pygame.QUIT:
         run = False
#  - обробка подій (натискання та відпускання клавіш)
      if event.type == pygame.KEYDOWN and setting.game_part=="game":
         key_name = pygame.key.name(event.key)
         if key_name in keys_rect:
            
            keys_sounds[key_name].set_volume(setting.volume)
          
            keys_sounds [key_name].play()
            keys_pressed.add(key_name)
      if event.type == pygame.KEYUP:
         key_name = pygame.key.name(event.key)
         keys_pressed.discard(key_name)  
#  - обробка кліку по клавішам  
      if event.type == pygame.MOUSEBUTTONDOWN and setting.game_part=="game":
         pos = event.pos
         for key, rect in keys_rect.items():
            if rect.collidepoint(pos) and not key in keys_pressed:
               
               keys_sounds[key].set_volume(setting.volume)
              
               keys_sounds[key].play()
               keys_pressed.add(key)
      if event.type == pygame.MOUSEBUTTONUP:
         pos = event.pos
         for key,rect in keys_rect.items():
            if rect.collidepoint(pos) and key in keys_pressed:
               keys_pressed.discard(key)
    
#  - відобразити фон, клавіши, оновити вікно
   window.fill(FON)
   '''виклич метод малювати меню'''
   setting.darw(window)
   '''перепиши список клавіш :
   виклич метод їх стоврення передавши значення кільксоті клавіш з меню'''

   '''додай умову - малювати якщо стангри=гра(перевір значення властивості меню)'''
   if setting.game_part == "game":
      draw_keys(window,keys_rect,keys_pressed)
 
   pygame.display.flip()
    # обробка лкіку по клавішам


