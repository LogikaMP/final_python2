# =====================
# ІМПОРТИ
# =====================
# customtkinter — UI
# settings — дані (теми, музика, рівні, діапазони)
# pygame.mixer — звук (ініціалізація мікшера)
import customtkinter as ctk
from settinhs import *
from pygame import mixer 

# =====================
# КЛАС MENU (ЕКРАН НАЛАШТУВАНЬ)
# =====================
class Menu(ctk.CTkFrame):

    def __init__(self, app):
        super().__init__(app)

        # =====================
        # 🔗 ПОСИЛАННЯ НА ГОЛОВНИЙ ДОДАТОК
        # =====================
        # через app ми:
        # - читаємо тему
        # - змінюємо рівень
        # - змінюємо музику
        # - повертаємось назад
        self.app = app
        self.configure(fg_color = self.app.temu['frame'])
        self.pack(expand = True, fill = "both", padx = 20,pady = 20 )

        # =====================
        # 📦 ОСНОВНИЙ ФРЕЙМ
        # =====================
        # займає все вікно
        # має фон теми
        # має відступи

        # =====================
        # 🏷 ЗАГОЛОВОК
        # =====================
        # текст "Налаштування"
        ctk.CTkLabel(self,text="Налаштування",text_color= self.app.temu["text"],
                     font=("Arial",36)).pack(pady = 10)
        
        # =====================
        # 🎨 БЛОК ТЕМИ
        # =====================
        # label "Тема"
        # dropdown (OptionMenu):
        # - значення беруться з settings_data["themes"]
        # - при зміні викликається chose_theme()
        ctk.CTkLabel(self,text="Тема",text_color= self.app.temu["text"],
                     font=("Arial",16)).pack(pady = 10)
        self.temu = ctk.CTkOptionMenu(self,values=settings_data["themes"],
                                      fg_color=self.app.temu["button"],
                                      text_color=self.app.temu["text"]
                                      ,button_color=self.app.temu["button_hover"],
                                      command=self.chose_theme)
        self.temu.pack(pady = 10)
        # =====================
        # 🎵 БЛОК МУЗИКИ
        # =====================
        # label "Фоновий звук"
        # dropdown:
        # - список музики
        # - при зміні викликається chose_music()
        ctk.CTkLabel(self,text="Фоновий звук",text_color= self.app.temu["text"],
                     font=("Arial",16)).pack(pady = 10)
        self.music = ctk.CTkOptionMenu(self,values=settings_data["music"],
                                      fg_color=self.app.temu["button"],
                                      text_color=self.app.temu["text"]
                                      ,button_color=self.app.temu["button_hover"],
                                      command=self.chose_music)
        self.music.pack(pady = 10)
        # =====================
        # 📊 БЛОК РІВНЯ
        # =====================
        # label "Рівень складності"
        # dropdown:
        # - список рівнів
        # - при зміні викликається chose_level()
        ctk.CTkLabel(self,text="Рівень складності",text_color= self.app.temu["text"],
                     font=("Arial",16)).pack(pady = 10)
        self.level = ctk.CTkOptionMenu(self,values=settings_data["levels"],
                                      fg_color=self.app.temu["button"],
                                      text_color=self.app.temu["text"]
                                      ,button_color=self.app.temu["button_hover"],
                                      command=self.chose_level)
        self.level.pack(pady = 10)
        # =====================
        # 🔊 БЛОК ГУЧНОСТІ
        # =====================
        # label "Гучність"
        # slider:
        # - діапазон з settings_data["volume_range"]
        # - при зміні викликається chose_volume()
        # - значення записується в app.volume
        # - одразу застосовується до mixer.music
        ctk.CTkLabel(self,text="Гучність",text_color= self.app.temu["text"],
                     font=("Arial",16)).pack(pady = 5)
        self.volume = ctk.CTkSlider(self,corner_radius=20,from_=settings_data["volume_range"][0],
                                    to=settings_data["volume_range"][1],command=self.chose_volume,)
        self.volume.pack(pady = 5)
        # =====================
        # 💾 КНОПКА "ЗБЕРЕГТИ"
        # =====================
        # при натисканні:
        # - викликається app.back_main()
        # - повертає користувача в головне меню
        ctk.CTkButton(self,text="Зберегти",fg_color=self.app.temu["button"],
                      corner_radius=25,
                      font=("Arial",16), border_color=self.app.temu["button_hover"],
                       border_width=5,
                      command=self.app.back).pack(pady=10)
        

    # =====================
    # 📊 ВИБІР РІВНЯ
    # =====================
    def chose_level(self, value):
        # знайти індекс вибраного рівня
        # взяти текст рівня з levels
        # записати в app.level
        pass


    # =====================
    # 🔊 ЗМІНА ГУЧНОСТІ
    # =====================
    def chose_volume(self, value):
        # отримати значення зі слайдера
        # записати в app.volume
        # застосувати через mixer.music.set_volume()
        pass


    # =====================
    # 🎨 ЗМІНА ТЕМИ
    # =====================
    def chose_theme(self, value):
        # знайти індекс теми
        # взяти тему з themes
        # записати в app.theme

        # ❗ важливо:
        # UI треба ПЕРЕМАЛЮВАТИ
        # - destroy старий Menu
        # - створити новий Menu

        # також оновити фон всього додатку
        pass


    # =====================
    # 🎵 ЗМІНА МУЗИКИ
    # =====================
    def chose_music(self, value):
        # знайти індекс музики

        # якщо "без музики":
        # - stop()
        # - app.music = None

        # інакше:
        # - записати назву файлу в app.music
        # - завантажити файл
        # - запустити цикл (-1)
        pass