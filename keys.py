'''Клавіші – логіка створення та відображення'''
from pygame import Rect, image, transform, mixer
from settings import*
from effects import draw_effect
from random import randint, shuffle
from sounds import missed_sound

mixer.init()
'''Клавіші – логіка створення та відображення'''
from pygame import Rect, image, transform, mixer
from settings import*
from effects import draw_effect
from random import randint, shuffle
from sounds import missed_sound

mixer.init()
# створюємо можливі позиції по висоті (без накладання)
def generate_y(num_keys):
    # загальна кількість позицій, які нам потрібні 
    # для всіх клавіш *100 (щоб було більше варіантів для перемішування)
    total = num_keys * 100
    # крок = висота клавіші + відступ
    step = 150  
    # створюємо список позицій по висоті, які йдуть з кроком вниз
    yy =
    # перемішуємо список, щоб клавіші з'являлися в різних місцях
   
    # повертаємо перемішаний список позицій
    

#додай аргумент level, щоб враховувати різні розміри клавіш на різних рівнях
#зміни функцію відповідно:
#1. Розмір та координату по х береом зі списків за номером рівня
#2. Додаємо цикл для створення клавіш на різних позиціях по висоті, 
# використовуючи згенеровані позиції з функції generate_y
def create_keys(num_keys):
    keys = {}
    x = X_KEY_START 
    data = dict(list(KEYS.items())[:num_keys ])
    # створюємо можливі позиції по висоті (без накладання)
    yy = 
    i = 0
    #цикл для створення клавіш на різних позиціях по висоті, використовуючи згенеровані позиції з функції generate_y
    
    for key in data:
        r = Rect(x, yy[i], KEY_WIDTH, KEY_HEIGHT)
        keys[key + str(i)] = r
        x += KEY_WIDTH +7
    return keys

def draw_keys(screen, keys, is_pressed):
    for key,rect in keys.items():
        pressed = key in is_pressed
        draw_effect(screen, rect, pressed)




#додай функцію для пошуку клавіші з найбільшою координатою по висоті,
#  яка не була натиснута, щоб перевіряти її при натисканні клавіші користувачем
def find_last_key(keys_rect, keys_pressed):



#додай функцію для руху клавіш вниз, 
# яка буде викликатися в основному циклі гри,
#  і видаляти клавіші, які вийшли за межі екрану,
#  а також перевіряти, чи була пропущена клавіша
def move_keys(keys_rect, keys_pressed):
    
    
    
    

    