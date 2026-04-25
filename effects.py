'''Ефекти – анімація клавіш і візуальні ефекти'''
from pygame import image,transform
from settings import BLACK, BLUE, GRAY, KEYS
key_up = image.load("assets/images/key_pressed.png")
key_down = image.load("assets/images/key_unpressed.png")




def draw_effect_sound(screen, sounds_img):
    for key, data in sounds_img.items():
        if data["draw"]:
            screen.blit(data['img'],(data['x'], data['y']))
            data['y'] -= 0.1
            if data['y'] <=0:
                data['y'] = data["start_y"]
                data["draw"] = False




def draw_effect(screen, rect, pressed):
    if pressed:
        img = key_up
    else:
        
        img = key_down
    img = transform.scale(img,(rect.w,rect.h))
    screen.blit(img,rect)

# 4. Створити функцію, що відображає ефекти на клавішах:
#  - отримати екран, де малювати
#  - отримати рект клавіші, на якій потрібно відобразити ефект
#  - отримати інформацію про те, чи клавіша натиснута
