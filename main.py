import customtkinter as ctk
from settinhs import *
from menu import Menu
from train import GameFrame
from pygame import mixer

class TypingApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Typing Trainer")
        self.geometry("600x500")
        self.resizable(False, False)
        self.theme = dark_theme
        self.music = None
        self.level = levels[0][0]
        self.volume = 0
        self.menu = None
        self.game= None

        # фон
        self.configure(fg_color=self.theme["bg"])

        # головний контейнер
        self.main_frame = ctk.CTkFrame(self, fg_color=self.theme["frame"], corner_radius=15)
        self.main_frame.pack(expand=True, padx=20, pady=20)

        # заголовок
        self.title_label = ctk.CTkLabel(
            self.main_frame,
            text="⌨️ Вітаємо у тренажері друку!",
            font=("Arial", 26, "bold"),
            text_color=self.theme["text"]
        )
        self.title_label.pack(pady=(30, 10))

        # опис
        self.desc_label = ctk.CTkLabel(
            self.main_frame,
            text="Перевір свою швидкість друку та прокачай навички 🚀",
            font=("Arial", 14),
            text_color=self.theme["secondary_text"]
        )
        self.desc_label.pack(pady=(0, 30))

        # кнопка старт
        self.start_button = ctk.CTkButton(
            self.main_frame,
            text="▶️ Старт",
            width=200,
            height=45,
            fg_color=self.theme["button"],
            hover_color=self.theme["button_hover"],
            text_color=self.theme["text"],
            command=self.start_game
        )
        self.start_button.pack(pady=10)

        # кнопка налаштування
        self.settings_button = ctk.CTkButton(
            self.main_frame,
            text="⚙️ Налаштування",
            width=200,
            height=45,
            fg_color=self.theme["accent"],
            hover_color="#e05570",
            text_color=self.theme["text"],
            command=self.open_settings
        )
        self.settings_button.pack(pady=10)

    # 🎮 дії
    def start_game(self):
        self.main_frame.pack_forget()
        self.game  = GameFrame(self)

    def open_settings(self):
        self.main_frame.pack_forget()
        self.menu = Menu(self)

    def back_main(self):
        mixer.music.stop()
        if self.menu:
            self.menu.destroy()
        if self.game:
            self.game.destroy()
        self.main_frame.pack(expand=True, padx=20, pady=20)
        


if __name__ == "__main__":
    app = TypingApp()
    app.mainloop()