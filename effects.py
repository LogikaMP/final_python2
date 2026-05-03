'''Ефекти – анімація клавіш і візуальні ефекти'''
from pygame import image,transform
from settings import BLACK, BLUE, GRAY, KEYS,path_img,X_KEY_START,Y_KEY_START,KEY_WIDTH
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
        


