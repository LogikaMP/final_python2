# Імпорт бібліотеки CustomTkinter для створення графічного інтерфейсу
# Імпорт головного меню застосунку
# Імпорт екрану караоке
from customtkinter import CTk
from menu import MenuFrame
from karaoke import Karaoke
from record_ui import RecordsFrame
import sounddevice as sd
# Створення головного класу застосунку
# Ініціалізація батьківського класу та налаштування фону
# Встановлення розміру вікна 600x600
# Встановлення назви вікна
# Змінна для збереження вибраної пісні (за замовчуванням перша)
# Створення та відображення головного меню
class App (CTk):
    def __init__ (self):
        super().__init__(fg_color="#310a31")
        self.geometry("600x600")
        self.title("karaoke")
        self.song = 0
        self.menu = MenuFrame(self)
        self.karaoke = None
        self.record_ui = None
        

# Функція переходу з меню в режим караоке
# Видаляємо головне меню з екрана
# Створюємо екран караоке
    def open_karaoke(self):
        self.menu.destroy()
        self.karaoke  = Karaoke(self)

    '''НОВЕ:метод вернутись назад:
    знишити караоке створити наново меню '''
    def back(self):
        if self.karaoke:
            self.karaoke.destroy()
        if self.record_ui:
            self.record_ui.destroy()
        sd.stop()
        self.menu = MenuFrame(self)

    '''НОВЕ:метод вілкрити вікно записів:
    знишити меню  створти вікно записів'''
    def open_record(self):
        self.menu.destroy()
        self.record_ui  = RecordsFrame (self)


App().mainloop()
# Створення та запуск застосунку