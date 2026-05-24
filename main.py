'''Main – запуск гри та обробка подій'''
# 6. Імпортуємо все що необхідно для роботи гри
import pygame
from settings import GRAY, WINDOW_WIDTH, WINDOW_HEIGHT, WHITE,GRAY,BLUE , FON
from keys import create_keys, draw_keys
from effects import load_sounds_img,move_sound_img,create_waves
from sounds import load_sounds, load_rand_sounds
'''Додай імопрт класу меню'''
from ui.settingsUi import SettingsMenu
# 7. Ініцилізація та Створити вікно 
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
fon = pygame.image.load(FON)
fon = pygame.transform.scale(fon,(WINDOW_WIDTH,WINDOW_HEIGHT))
setting = SettingsMenu(10,10,100,40,GRAY,WHITE,BLUE)
# 8. Створити список ректів - клавіш
keys_rect = create_keys(setting.num_keys)

# 9. Створити порожню множину - натиснуті клавіши
keys_pressed = set()
# 10. Створити список звуків - завантажити звуки нот
'''НОВЕ:перевір значення on_rand_sound меню setting:
якщо правда - завантаж випадкові звуки, 
якщо ні - звичанів '''
if setting.on_rand_sound:
   keys_rand_sounds = load_rand_sounds()
else:
   keys_rand_sounds = None
sound_img= load_sounds_img()
list_sound_img = []


keys_sounds = load_sounds()
keys_rand_sounds = load_rand_sounds()
''''''

sound_img= load_sounds_img()
list_sound_img = []
'''НОВЕ:Виклич функцію що створить хвилі - waves'''
waves = create_waves()


''''''
'''Створи обєкт меню:
координати - 20,20,
розмір - 100, 40
кольри - GREY, WHITE, BLUE'''
setting = SettingsMenu(20,20,100,40,GRAY,WHITE,BLUE)

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
      '''НОВЕ:перевір значення on_rand_sound меню setting:
         якщо правда - завантаж випадкові звуки, 
         якщо ні - звичанів '''
      if setting.on_rand_sound:
         keys_rand_sounds = load_rand_sounds()
      else:
         keys_rand_sounds = None
         sound_img = load_sounds_img()
         list_sound_img = []

      
        
      if event.type == pygame.QUIT:
         run = False
#  - обробка подій (натискання та відпускання клавіш)
      if event.type == pygame.KEYDOWN and setting.game_part=="game":
         key_name = pygame.key.name(event.key)
         if key_name in keys_rect:
            
            keys_sounds[key_name].set_volume(setting.volume)
            waves[key_name].play()
            if setting.on_rand_sound:
               keys_rand_sounds[key_name].set_volume(setting.volume) 
               keys_rand_sounds[key_name].play()
            else:
               keys_sounds [key_name].play()
            '''НОВЕ:виклич для відповідної хвиді мтеod    грати'''

            list_sound_img.append(sound_img[key_name].copy())
            keys_pressed.add(key_name)
      if event.type == pygame.KEYUP:
         key_name = pygame.key.name(event.key)
         keys_pressed.discard(key_name)  
#  - обробка кліку по клавішам  
      if event.type == pygame.MOUSEBUTTONDOWN and setting.game_part=="game":
         pos = event.pos
         for key, rect in keys_rect.items():
            if rect.collidepoint(pos) and not key in keys_pressed:
               waves[key].play()
               keys_sounds[key].set_volume(setting.volume)
               if setting.on_rand_sound:
                  keys_rand_sounds[key].set_volume(setting.volume) 
                  keys_rand_sounds[key].play()
               else:
                  keys_sounds[key].play()
               '''НОВЕ:виклич для відповідної хвиді мтеod    грати'''

               list_sound_img.append(sound_img[key].copy())
               keys_pressed.add(key)
      if event.type == pygame.MOUSEBUTTONUP:
         pos = event.pos
         for key,rect in keys_rect.items():
            if rect.collidepoint(pos) and key in keys_pressed:
               keys_pressed.discard(key)
    
#  - відобразити фон, клавіши, оновити вікно
   window.blit(fon,(0,0))
   '''виклич метод малювати меню'''
   setting.darw(window)
   '''перепиши список клавіш :
   виклич метод їх стоврення передавши значення кільксоті клавіш з меню'''

   '''додай умову - малювати якщо стангри=гра(перевір значення властивості меню)'''
   if setting.game_part == "game":
      '''НОВЕ:Перебери словник хвиль:
      кожну намалюй, онови'''
      for wave in waves.values():
            wave.draw(window)
            wave.update()
      
      

      
      draw_keys(window,keys_rect,keys_pressed)
      move_sound_img(list_sound_img,window)
   pygame.display.flip()
   fps = 60
   pygame.time.Clock().tick(fps)
    # обробка лкіку по клавішам


