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
    yy = [-i * step for i in range(total)]
    # перемішуємо список, щоб клавіші з'являлися в різних місцях
    shuffle(yy)
    # повертаємо перемішаний список позицій
    return yy

#додай аргумент level, щоб враховувати різні розміри клавіш на різних рівнях
#зміни функцію відповідно:
#1. Розмір та координату по х береом зі списків за номером рівня
#2. Додаємо цикл для створення клавіш на різних позиціях по висоті, 
# використовуючи згенеровані позиції з функції generate_y
def create_keys(num_keys, level):
    keys = {}
    x = X_KEY_START 
    data = dict(list(KEYS.items())[:num_keys ])
    # створюємо можливі позиції по висоті (без накладання)
    yy = generate_y(num_keys)
    i = 0
    #цикл для створення клавіш на різних позиціях по висоті, використовуючи згенеровані позиції з функції generate_y
    x = X_KEY_START [level]
    while i < len(yy):
        for key in data:
            r = Rect(x, yy[i], KEY_WIDTH[level], KEY_HEIGHT[level])
            keys[key + str(i)] = r
            x += KEY_WIDTH[level] +7
            i += 1
        x = X_KEY_START[level]
    return keys

def draw_keys(screen, keys, is_pressed):
    for key,rect in keys.items():
        pressed = key in is_pressed
        draw_effect(screen, rect, pressed)




#додай функцію для пошуку клавіші з найбільшою координатою по висоті,
#  яка не була натиснута, щоб перевіряти її при натисканні клавіші користувачем
def find_last_key(keys_rect, keys_pressed):
    last_key = None
    for key in keys_rect:
        if key in keys_pressed:
            continue
        if not last_key:
            last_key = key
        if keys_rect[key].y > keys_rect [last_key].y:
            last_key = key
    return last_key    


#додай функцію для руху клавіш вниз, 
# яка буде викликатися в основному циклі гри,
#  і видаляти клавіші, які вийшли за межі екрану,
#  а також перевіряти, чи була пропущена клавіша
def move_keys(keys_rect, keys_pressed):
    for key in keys_rect.copy():
        keys_rect[key].y += SPEED
        if keys_rect[key].y > WINDOW_HEIGHT:
            del keys_rect[key]
            if key in keys_pressed:
                keys_pressed.remove(key)
            else:
                    missed_sound.play()
    
    
    

    