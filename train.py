# =====================
# ІМПОРТИ
# =====================
import customtkinter as ctk
from tkinter import Text
from pygame import mixer
import time
import random
from settinhs import *


# =====================
# КЛАС ГРИ (ЕКРАН ДРУКУ)
# =====================
class GameFrame(ctk.CTkFrame):

    def __init__(self, app):
        super().__init__(app)
        self.app = app
        self.configure(fg_color=self.app.temu["bg"])
        self.pack(expand=True, fill="both", padx=20, pady=20)

        # =====================
        # 🎮 СТАН ГРИ
        # =====================
        self.used_texts = set()
        self.text = self.choose_text()
        self.index = 0
        self.start_time = None
        self.finished = False
        self.errors = 0
        self.timer_id = None

        # =====================
        # 📊 ВЕРХНЯ ПАНЕЛЬ
        # =====================
        frame_info = ctk.CTkFrame(self, fg_color=self.app.temu["frame"])
        frame_info.pack(pady=10, fill="x")

        ctk.CTkLabel(frame_info, text=f"Всього: {len(self.text)}", 
                     text_color=self.app.temu["text"]).pack(side="left", padx=10)
        
        self.label_count = ctk.CTkLabel(frame_info, text="Надруковано: 0",
                                       text_color=self.app.temu["text"])
        self.label_count.pack(side="left", padx=10)
        
        self.label_timer = ctk.CTkLabel(frame_info, text="Час: 0.0 сек",
                                       text_color=self.app.temu["text"])
        self.label_timer.pack(side="left", padx=10)

        self.label_mode = ctk.CTkLabel(frame_info, text=f"Режим: {self.app.mode}",
                                       text_color=self.app.temu["accent"])
        self.label_mode.pack(side="left", padx=10)

        # =====================
        # 📝 ВВЕДЕНИЙ ТЕКСТ
        # =====================
        self.label_input = ctk.CTkLabel(self, text="Введіть текст...",
                                       text_color=self.app.temu["accent"],
                                       font=("Arial", 14, "bold"))
        self.label_input.pack(pady=10)

        # =====================
        # 📄 ТЕКСТ ДЛЯ ДРУКУ
        # =====================
        self.textbox = Text(self, height=10, width=60, 
                           bg=self.app.temu["frame"],
                           fg=self.app.temu["text"],
                           state="disabled",
                           font=("Arial", 12))
        self.textbox.pack(pady=10)
        
        # Налаштування тегів для правильних/неправильних символів
        self.textbox.tag_configure("correct", foreground=self.app.temu["accent"], font=("Arial", 12, "bold"))
        self.textbox.tag_configure("wrong", foreground="#FF0000", font=("Arial", 12, "bold"))
        self.textbox.tag_configure("current", background=self.app.temu["button"], foreground=self.app.temu["text"], font=("Arial", 12, "bold"))
        
        # Вставити текст
        self.textbox.config(state="normal")
        self.textbox.insert("1.0", self.text)
        self.textbox.config(state="disabled")

        # =====================
        # 🎮 КНОПКИ
        # =====================
        frame_btn = ctk.CTkFrame(self, fg_color=self.app.temu["frame"])
        frame_btn.pack(pady=10)

        ctk.CTkButton(frame_btn, text="Меню", 
                     fg_color=self.app.temu["button"],
                     text_color=self.app.temu["text"],
                     command=self.app.back).pack(side="left", padx=5)
        
        ctk.CTkButton(frame_btn, text="Повторити",
                     fg_color=self.app.temu["button"],
                     text_color=self.app.temu["text"],
                     command=self.restart).pack(side="left", padx=5)

        # =====================
        # ⌨️ ОБРОБКА КЛАВІАТУРИ
        # =====================
     
        self.app.bind("<Key>", self.key_press)

        # =====================
        # 🎵 МУЗИКА
        # =====================
        self.handle_music()

        # =====================
        # ⏱ ЗАПУСК ТАЙМЕРА
        # =====================
        self.update_timer()


    # =====================
    # ⌨️ ОБРОБКА НАТИСКАНЬ
    # =====================
    def key_press(self, event):
        if self.finished:
            if event.keysym == "Return":
                self.restart()
            return
        
        if self.start_time is None:
            self.start_time = time.time()
        
        if self.index >= len(self.text):
            self.finished = True
            self.show_res()
            return
        
        expected_char = self.text[self.index]
        entered_char = event.char
        
        if len(entered_char) == 0:
            return
        
        self.textbox.config(state="normal")
        # Видалити попередню підсвітку
        self.textbox.tag_remove("current", "1.0", "end")
        self.textbox.tag_remove("wrong", f"1.{self.index}", f"1.{self.index + 1}")
        
        if entered_char == expected_char:
            self.textbox.tag_add("correct", f"1.{self.index}", f"1.{self.index + 1}")
            self.index += 1
        else:
            self.textbox.tag_add("wrong", f"1.{self.index}", f"1.{self.index + 1}")
            self.errors += 1
            if self.app.mode == settings_data["modes"][1]:
                self.label_input.configure(text="Помилка! Введи правильний символ")
                self.textbox.tag_add("current", f"1.{self.index}", f"1.{self.index + 1}")
                self.textbox.config(state="disabled")
                return
            self.index += 1

        # Підсвітити наступний символ
        if self.index < len(self.text):
            self.textbox.tag_add("current", f"1.{self.index}", f"1.{self.index + 1}")

        self.textbox.config(state="disabled")
        # Показати введений текст
        entered_so_far = self.text[:self.index]
        self.label_input.configure(text=f"Введено: {entered_so_far}")
        self.label_count.configure(text=f"Надруковано: {self.index}")


    def choose_text(self):
        if self.app.level == len(levels):
            options = []
            for level_texts in levels:
                options.extend(level_texts)
        else:
            options = levels[self.app.level]

        if len(options) == 0:
            return ""

        unused_texts = [text for text in options if text not in self.used_texts]
        if not unused_texts:
            self.used_texts.clear()
            unused_texts = options[:]

        text = random.choice(unused_texts)
        self.used_texts.add(text)
        return text

    # =====================
    # 🏁 ПОКАЗ РЕЗУЛЬТАТУ
    # =====================
    def show_res(self):
        elapsed_time = time.time() - self.start_time
        speed = len(self.text) / elapsed_time if elapsed_time > 0 else 0
        
        self.textbox.config(state="normal")
        self.textbox.delete("1.0", "end")
        
        result_text = f"""
╔════════════════════════════════════╗
║        ✅ГОТОВО!                  ║ 
╠════════════════════════════════════╣
║ Час:           {elapsed_time:.2f} с║
║ Символів:      {len(self.text)} шт ║
║ Швидкість:     {speed:.2f} сим/сек ║
║ Помилок:       {self.errors} шт    ║
╚════════════════════════════════════╝
        """
        self.textbox.insert("1.0", result_text)
        self.textbox.config(state="disabled")


    # =====================
    # 🎵 МУЗИКА
    # =====================
    def handle_music(self):
        if self.app.music == settings_data["music"][0]:
            return

        if mixer.music.get_busy():
            return

        try:
            music_index = settings_data["music"].index(self.app.music)
            music_file = musics[music_index]
            mixer.music.load(music_file)
            mixer.music.set_volume(self.app.volume)
            mixer.music.play(-1)
        except Exception as e:
            print(f"Помилка музики: {e}")


    # =====================
    # 🔁 ПЕРЕЗАПУСК
    # =====================
    def restart(self):
        self.text = self.choose_text()
        self.index = 0
        self.start_time = None
        self.finished = False
        self.errors = 0
        
        self.textbox.config(state="normal")
        self.textbox.delete("1.0", "end")
        self.textbox.insert("1.0", self.text)
        self.textbox.config(state="disabled")
        
        self.label_input.configure(text="Введіть текст...")
        self.label_count.configure(text="Надруковано: 0")
        self.label_timer.configure(text="Час: 0.0 сек")
        self.label_mode.configure(text=f"Режим: {self.app.mode}")
        
        if self.timer_id:
            self.after_cancel(self.timer_id)
        self.update_timer()


    # =====================
    # ⏱ ТАЙМЕР
    # =====================
    def update_timer(self):
        if self.start_time is not None and not self.finished:
            elapsed = time.time() - self.start_time
            self.label_timer.configure(text=f"Час: {elapsed:.1f} сек")
        
        self.timer_id = self.after(100, self.update_timer)
