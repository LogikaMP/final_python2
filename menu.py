import pygame
from buttons import Button
from settings import*
'''3. Створи лкас меню'''
class Menu:
    '''Консруткор приймає координати та розмір'''
    def __init__(self,x,y,w,h):
        '''створити змінні -властивості:
        music - номер музики
        fon_music - вкл-викл музики
        level  - номер рівня 
        back_start - прапор назад до старту-вікна
        '''
        self.music = 0
        self.fon_music= False
        self.level = 0
        self.back_start = False
        '''Створити 4 кнопки:
        координати: х = х, у = у,y+h+15,y+2*h+30, y+3*h+45
        розмір - w, h, колір - BLUE,GREY,
        тексти - Fon music: off,Music: off, Level: 1,  Back
        команди - відповідні   '''
        self.btn_music = Button( x,y,w,h,GREY,"Music: off",BLUE,command=self.chose_music)  
        self.btn_on_of = Button( x,y+h+15,w,h,GREY,"Fon music: off",BLUE,command=self.on_off_fon)
        self.btn_level = Button( x,y+2*h+30,w,h,GREY,"Level: 1",BLUE,command=self.chose_level)
        self.btn_back  = Button( x,y+3*h+45,w,h,GREY,"Back",BLUE,command=self.back)

    

    '''Метод оновлення меню - малюємо кнопки , виклик кліка по кнопках'''
    def update(self, window):
        self.btn_music.draw(window)
        self.btn_on_of.draw(window)
        self.btn_level.draw(window)
        self.btn_back.draw(window)
        self.btn_music.is_clicked()
        self.btn_on_of.is_clicked()
        self.btn_level.is_clicked()
        self.btn_back.is_clicked()
      
    '''Метод вибору пісня'''
    def chose_music(self):
        self.music += 1
        if self.music == len(FON_MUSICS):
            self.music = 1
        self.btn_music.add_text( f"Music: {FON_MUSICS[self.music]}")
        
    '''Метод вклю викл музики'''    
    def on_off_fon(self):
        if self.fon_music:
            self.btn_on_of.add_text ( "Fon music: on")
            self.fon_music = False
        else:
            self.btn_on_of.add_text ( "Fon music: off")
            self.fon_music = True
        
    '''Метод вибору рівня'''
    def chose_level(self):
        self.level += 1
        if self.level == len(LEVELS):
            self.level = 0
        self.btn_level.add_text(f"Level: {LEVELS[self.level]}")
    
    '''Метод повренутись назад'''
    def back(self):
        self.back_start = True
