import pygame
from buttons import Button
from settings import*
'''3. Створи лкас меню'''
class Menu:
    '''Консруткор приймає координати та розмір'''
    def 
        '''створити змінні -властивості:
        music - номер музики
        fon_music - вкл-викл музики
        level  - номер рівня 
        back_start - прапор назад до старту-вікна
        '''
       
        '''Створити 4 кнопки:
        координати: х = хб у = у,y+h+15,y+2*h+30, y+3*h+45
        розмір - w, h, колір - BLUE,GREY,
        тексти - Fon music: off,Music: off, Level: 1,  Back
        команди - відповідні   '''
        self.btn_music 
        self.btn_on_of 
        self.btn_level 
        self.btn_back 
    

    '''Метод оновлення меню - малюємо кнопки , виклик кліка по кнопках'''
    def update(self, window):
      
    '''Метод вибору пісня'''
    def chose_music(self):
        
    '''Метод вклю викл музики'''    
    def on_off_fon(self):
        
    '''Метод вибору рівня'''
    def chose_level(self):
    
    '''Метод повренутись назад'''
    def back(self):
        self.back_start = True