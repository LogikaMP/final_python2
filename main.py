
import pygame
from settings import *
from buttons import Button
from effects import draw_effect, draw_start
from keys import create_keys, draw_keys, move_keys, find_last_key
from sounds import*

#додай функцію start(), яка буде запускати гру,
#  і викликати функцію для створення клавіш на основі поточного рівня,
#  а також встановлювати фонову музику для цього рівня
def start(i):
   global game_part, fon_game, keys_rect
   draw_start(window,200,50)
   game_part = "game"
   fon_game = pygame.image.load(images_path + LEVELS[i])
   fon_game = pygame.transform.scale(fon_game, (WINDOW_WIDTH, WINDOW_HEIGHT))
   pygame.mixer.music.load(sounds_path + FON_SOUND[i])
   pygame.mixer.music.set_volume(0.1)
   pygame.mixer.music.play(-1)
   keys_rect = create_keys(LEVELS_KEYS[i],i)
   game_part = "game"



pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
#завантажуємо фонову картинку для стартового екрану
fon_start = pygame.image.load(images_path + FON_START)
fon_start = pygame.transform.scale(fon_start,(WINDOW_WIDTH, WINDOW_HEIGHT))
#стоври зміну для фону гри, список клавіш
fon_game = None
keys_rect = None
start_txt = Button(100,20,300,50,(40,98,250),"Обери рівень складності",(38,91,105),None)
keys_pressed= set()
keys_sounds = load_sounds()

#створи кнопку запуску гри на стартовому екрані, яка буде викликати функцію start() при натисканні
#координати 150, 150, розмір 200 на 100, колір (40, 98, 250), текст "Start", колір тексту (38, 91, 105)

btn_levels = [] 
for i in range(5):
   b = Button(BTN_LEVELS_X [i], BTN_LEVELS_Y [i], 100, 50, (40,98,250), str(LEVELS_KEYS[i]),(38,91,105),lambda i = i: start(i))
   btn_levels.append(b)
run = True
#змінна для відстеження поточної частини гри (старт, гра, кінець)
game_part = "start"
#змінна для відстеження поточного рівня, таймера та кількості пропущених клавіш
level = 0
timer = 0
miss = 0
# кнопка-текст для відображення таймера та кількості пропущених клавіш під час гри
#координати 10, 10, розмір 70 на 40, колір (40, 98, 250), текст "Time: {timer}", колір тексту (38, 91, 105)
#координати 10, 60, розмір 70 на 40, колір (40, 98, 250), текст "Miss: {miss}", колір тексту (38, 91, 105)
#btn_timer 
#bnt_miss 
#end 
while run:
   #додай перевірку для відображення різних частин гри (старт, гра, кінець) та виклику відповідних функцій для відображення екрану та обробки логіки гри
   #якщо старт - фон, кнопка старту, перевірка кліку по кнопці
   #якщо гра - фон рівня, відображення клавіш, рух клавіш, відображення таймера та пропущених клавіш, перевірка на кінець рівня або гри
   if game_part == "start":
      window.blit(fon_start,(0,0))
      for btn in btn_levels:
         btn.draw(window)
         btn.is_clicked()
      start_txt.draw(window)
   if game_part == "game":
      window.blit(fon_game,(0,0))
      draw_keys(window,keys_rect,keys_pressed)
      move_keys(keys_rect,keys_pressed)
      if len(keys_rect) == 0:
         pygame.mixer.music.stop()
         game_part = "start"

   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         run = False

      if event.type == pygame.MOUSEBUTTONDOWN:
         if game_part == "game":
            pos = event.pos
            last_key = find_last_key(keys_rect, keys_pressed)
            if keys_rect [last_key].collidepoint(pos):
               keys_pressed.add(last_key)
               s = last_key[0]
               keys_sounds [s].play()
            else:
               wrong_sound.play()
            #знайти клавішу з найбільшою координатою по висоті, яка не була натиснута, щоб перевіряти її при натисканні клавіші користувачем
            # первір чи по ній клікнуто
            # якщо так - додай її до натиснутих, відтворити звук клавіші
            # якщо ні - відтворити звук помилки та збільшити лічиль
              
            

            


   pygame.display.flip()
   clock.tick(60)
    # обробка лкіку по клавішам


