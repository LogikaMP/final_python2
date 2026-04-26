'''Клас меню налаштування - гучності та кількості клавіш'''
# імпортуй клас кнопки
# імпортуй клас повзунка
# імпортуй список клавіш
from buttons import Button
from ui.slider import Slider
from settings import KEYS,BLACK, GRAY, BLUE
# клас меню налаштувань. Аргументи:
# координати для кнокпи налаштування та розміри
# кольри: кнопки, тексту, слайдера
class SettingsMenu:                 
    def __init__(self,x,y,w,h,col_btn,col_txt,col_slider): 
        # створи кнопку відкриття меню налаштувань: 

        # координати, розмір, кольри - з конструктора класу, 
        # текст -"Setting" , 
        # команда - відкрити меню
        self.btn_open = Button(x,y,w,h,col_btn,"Settings",col_txt,command= self.open_menu,image="assets/images/buttons/settings_hover.png")
        # створи кнопку повернення назад
        # координати, розмір, кольри - з конструктора класу, 
        # текст -"Back" , 
        # команда - закрити меню
        self.btn_close = Button(x,y,w,h,col_btn,"Back",col_txt,command= self.close_menu,image="assets/images/buttons/exit_hover.png")
        # змісти координати для розміщення елементів меню - тексти+слайдери, 
        # х = ч + половина висоти, у = у + ширина
        x = x + h//2
        y = y + w
    

        # створи текстову кнопку (підпис) для гучності: 
        # координати - що розрахували вище, 
        # текст = "Volume", команди = немає
        self.txt_volume = Button(x,y,w,h,col_btn,"volume",color_text=BLACK,command=None)
        
        # обчисли позицію для повзунка (праворуч від тексту), 
        # х2 = права координата текстової кнокпи + половина висоти
        x2 = self.txt_volume.rect.right + h//1.5
        
        # трохи змісти вниз для кращого вирівнювання : у = у + чверть висоти
        y = y + h//4

        # створи повзунок гучності : 
        # координати - ті що розрахували вище, 
        # ширина = три ширина, 
        # висота = половина висоти
        # (від 0 до 101)
        self.slider_volume = Slider(x2,y,w*3,h//2,max_num=100,col=col_slider,col_pointer=col_btn)
       
        # створи змінну для збереження гучності = 0
        self.volume = 0 

        # змісти вниз для наступного блоку= у + дві вистоти
        y = y + h*2
 
        # створи текст для кількості клавіш: 
        # координати - що розрахували вище, 
        # текст = "Num keys", команди = немає
        self.txt_num_keys = Button(x,y,w,h,col_btn,text="Num keys",color_text="BLACK",command=None)
 
        # трохи змісти вниз : у = у + чверть висоти
  
        # створи повзунок кількості клавіш
        # координати - ті що розрахували вище(х2, у), 
        # ширина = три ширина, 
        # висота = половина висоти
        # (від 0 до кількості клавіш KEYS+1)
        self.slider_num_keys = Slider(x2,y+h//3,w*3,h//2,max_num=7,col=col_slider,col_pointer=col_btn)
        self.num_keys = 0
        # створи змінну для збереження кількості клавіш = 0
        self.rand = False
        y = y + h*2
        self.btn_rand_text = Button(x2+w//3,y,w,h,col_btn,text="Rand sound",color_text="BLACK",command=None)
        self.btn_rand = Button(x2+w//3+w+10, y,h,h,col_btn,"-",col_btn,self.active_rand )
        # задай початковий стан (гра)= властивість game_part = "game"
        self.game_part = "game"

    def active_rand(self):
        if self.rand:
            self.rand = False
            self.btn_rand.color = GRAY
            self.btn_rand.add_text("-")
        else:
            self.rand = True 
            self.btn_rand.color =BLUE
            self.btn_rand.add_text("X")
    def open_menu(self):
        # переключи стан на меню налаштувань
        self.game_part = "settings"
    def close_menu(self): 
        # поверни стан назад до гри
        self.game_part = "game"

    # метод відображення кнопок  та сладйерів меню
    def darw(self, window):
        # якщо стан гри = гра
        if self.game_part == "game":
            # намалюй кнопку налаштувань
            self.btn_open.draw(window)
        # якщо стан гри = налащтування
        if self.game_part == "settings":
            # намалюй кнопку назад
            self.btn_close.draw(window)
            # намалюй текст гучності
            self.txt_volume.draw(window)
          
            # намалюй повзунок гучності
            self.slider_volume.draw(window)
            # намалюй текст кількості клавіш
            self.txt_num_keys.draw(window)

            # намалюй повзунок кількості клавіш
            self.slider_num_keys.draw(window)
            self.btn_rand_text.draw(window)
            self.btn_rand.draw(window)

           
    #метод оновлення меню
    def update(self, event=None):
        # якщо стан гри = гра
         if self.game_part == "game" :   
            # перевір натискання кнопки налаштувань
            self.btn_open.is_clicked()
        # якщо стан гри = налащтування
         if self.game_part == "settings":
        
            # перевір натискання кнопки назад
            self.btn_close.is_clicked()
            self.btn_rand.is_clicked()
            # оброби перетягування повзунка гучності
            if event:
                self.slider_volume.update(event=event)
                self.slider_num_keys.update(event=event)
          
            # оброби перетягування повзунка клавіш
            self.volume = self.slider_volume.value/100
            self.num_keys = self.slider_num_keys.value


            # 0 - 1 (нормалізація гучності) : значення сладйера гучності  / 100 
            #  

            # збережи вибрану кількість клавіш