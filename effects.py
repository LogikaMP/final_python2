'''Ефекти – анімація клавіш і візуальні ефекти'''
from pygame import image,transform, draw
from settings import BLACK, BLUE, GRAY, KEYS,path_img,X_KEY_START,Y_KEY_START,KEY_WIDTH, WINDOW_HEIGHT, WINDOW_WIDTH
import math
import random

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
def load_sounds_img():
    sound_img = {}
    x = X_KEY_START + 15
    y = Y_KEY_START
    for key in KEYS:
        img = image.load(path_img + "notes/"+key+".png")
        img = transform.scale(img,(25,50))
        sound_img[key]={"img":img,
                        "x":x,
                        "y":y
                        }
        x += KEY_WIDTH + 10
    return sound_img
def move_sound_img(sounds_img_list,screen):
    for img in sounds_img_list.copy():
        img["y"]-= 1
        if img["y"] < 0:
            sounds_img_list.remove(img)
            return
        screen.blit(img["img"],(img["x"],img["y"]))

def random_color():
    return (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255)
    )  
'''НОВЕ: Створи клас для хвилі - приймає колір та коордианту у'''
class Wave:
    def __init__(self):
        pass
        ...
        '''збережи колір та координату у'''
       
        '''встанови амплітуду хвилі(властивість) на 10 та потчону амплітуду на 10'''
        

        '''встанови властивість швидоксті на 0.05'''
        
        '''Встанвои відступ - випадковий від 0 до 1000'''
       

    '''Створи мтеод виклику хвилі-звуку
    міняє потчону амплітуду на випадкове число '''
    def play(self):
        ...

    '''Створи мтеод оновленя хвилиі - плавного затухання'''
    def update(self):
        '''додаємо до амплітуди різницю поточної амплітуди та просто амплітуди помножити на 0.1
        (поточна амплітуда - амплітуда)*0.1'''
        '''зміни потчону амплітуду - помнож на 0.92'''
        
        '''зміни відступ на +4'''
       
    '''Створи мтеод малювання хвилі на вікні'''
    def draw(self, screen):
        ...
        '''створи список крапочок'''
        
        '''цикл для перебору х від 0, до ширини екрану з кроком 8'''
        
            '''розраху коордианту у:
            стартова координата у + math.sin((x + відступ)* ШВИДКІСТЬ) + амплітуда
            '''
           
            '''Додай кортеж з координат у список крапочк'''
             
        '''Намалюй лінію за координатами з крапочок 
        draw.lines(вікно, колір,False, список крапок, 4)
        '''
        


'''Створи функці для створення словника хвиль
для кожної клавіши - своя хвиля
перебираємо словник лкавіш - щоб отримати ключ для хвилі
починаємо з коордианти у = 210, для кожної наступнох -20
колір випадковий
повернути словник хвиль'''


