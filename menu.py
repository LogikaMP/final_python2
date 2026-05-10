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
                                      text_color=self.app.temu["text"],
                                      button_color=self.app.temu["button_hover"],
                                      command=self.chose_theme)
        self.temu.pack(pady = 10)
        self.temu.set(settings_data["themes"][self.app.theme])
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
                                      text_color=self.app.temu["text"],
                                      button_color=self.app.temu["button_hover"],
                                      command=self.chose_music)
        self.music.pack(pady = 10)
        self.music.set(self.app.music)
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
                                      text_color=self.app.temu["text"],
                                      button_color=self.app.temu["button_hover"],
                                      command=self.chose_level)
        self.level.pack(pady = 10)
        self.level.set(settings_data["levels"][self.app.level])
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
        self.volume.set(self.app.volume)
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
    # знайти індекс вибраного рівня
    # взяти текст рівня з levels
    # записати в app.level
    def chose_level(self, value):
        i = self.level.get() # отримуємо текст з dropdown
        self.app.level = settings_data["levels"].index(i) # знаходимо індекс і записуємо в app.level


        



    # =====================
    # 🔊 ЗМІНА ГУЧНОСТІ
    # =====================
    def chose_volume(self, value):
        # отримати значення зі слайдера
        # записати в app.volume
        # застосувати через mixer.music.set_volume()
        self.app.volume = self.volume.get() # отримуємо значення слайдера і записуємо в app.volume
        mixer.music.set_volume(self.app.volume) # застосовуємо гучність до муз


    # =====================
    # 🎨 ЗМІНА ТЕМИ
    # =====================
    def chose_theme(self, value):
        # знайти індекс теми
        # взяти тему з themes
        # записати в app.theme
        self.app.theme = settings_data["themes"].index(self.temu.get())
        self.app.temu = themes[self.app.theme]

        # оновити фон всього додатку
        self.app.configure(fg_color=self.app.temu["bg"])
        if hasattr(self.app, "frame") and self.app.frame:
            self.app.frame.configure(fg_color=self.app.temu["frame"])

        # перезавантажити Menu UI з новою темою
        self.destroy()
        self.app.menu = Menu(self.app)



    # =====================
    # 🎵 ЗМІНА МУЗИКИ
    # =====================
    def chose_music(self, value):
        selected_music = self.music.get()
        
        # якщо "Вимкнено" (перший варіант):
        if selected_music == settings_data["music"][0]:
            mixer.music.stop()
            self.app.music = settings_data["music"][0]
        else:
            # інакше:
            # - знайти індекс музики
            # - взяти назву файлу з musics
            # - завантажити файл
            # - встановити гучність
            # - запустити з циклом (-1)
            music_index = settings_data["music"].index(selected_music)
            music_file = musics[music_index]
            
            try:
                mixer.music.load(music_file)
                mixer.music.set_volume(self.app.volume)
                mixer.music.play(-1)
                self.app.music = selected_music
            except Exception as e:
                print(f"Помилка при завантаженні музики: {e}")
                self.app.music = settings_data["music"][0](-1)
        