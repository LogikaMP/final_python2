from customtkinter import CTk, CTkButton, CTkLabel, CTkCanvas, CTkFrame
import sounddevice as sd
from scipy.io import wavfile
import os
import numpy as np
from random import randint
from settings import *


class Karaoke(CTkFrame):
    def __init__(self, app):
        super().__init__(app, fg_color="transparent")

        # стан запису та відтворення
        self.recording = False
        self.playing = False
        self.app = app

        # шлях до мінусовки
        self.minus = os.path.join(minus_path, minus[self.app.song])
        '''НОВЕ:'''
        # НОВЕ: Додай кнопку 🔙 кнопка назад (верхній правий кут) 
        # текст "⬅️"б розмір 60 на 40 колір "#3c80bc" 
        # команда self.app.back 
        # розаташування place(relx=1.0, x=-10, y=10, anchor="ne")
        CTkButton(
            self,
            text="⬅️",
            width=60,
            height=40,
            fg_color="#3c80bc",
            corner_radius=10,
            border_color="#061076",
            border_width=2,
            command=self.app.back
        ).place(relx=1.0, x=-10, y=10, anchor="ne")

        self.pack(fill="both", expand=True)

        # заголовок
        lbl = CTkLabel(
            self,
            text="Simple Karaoke",
            text_color="#BF9BC6",
            font=("Arial", 40)
        )
        lbl.pack(pady=30)

        # кнопка запису
        self.btn_record = CTkButton(
            self,
            text="Start",
            width=200,
            height=100,
            fg_color="#C52EA7",
            corner_radius=50,
            border_color="#BC8CB7",
            border_width=10,
            command=self.do_record
        )
        self.btn_record.bind("<Button-3>", self.stop_all)  # правий клік = стоп
        self.btn_record.pack()

        # інформаційний текст
        self.lbl_info = CTkLabel(
            self,
            text="Start record + minus",
            text_color="#DABBD5",
            font=("Arial", 16)
        )
        self.lbl_info.pack()

        lbl2 = CTkLabel(
            self,
            text="Left click stop all",
            text_color="#DABBD5",
            font=("Arial", 16)
        )
        lbl2.pack()

        # створення візуалізації звуку
        self.creat_anime_sound()

        # текст пісні (тінь)
        self.canva.create_text(
            442, 252,
            text=texts[self.app.song],
            fill="#5a2a50",
            font=("Arial", 12, "bold"),
            anchor="center"
        )

        # текст пісні (основний)
        self.canva.create_text(
            440, 250,
            text=texts[self.app.song],
            fill="#e494d9",
            font=("Arial", 12, "bold"),
            anchor="center"
        )

    # зупинка всього (звук + запис)
    def stop_all(self, e):
        sd.stop()
        self.playing = False
        self.recording = False
        self.btn_record.configure(text="Start")
        self.lbl_info.configure(text="Processing and saving...")

    # створення візуалізації аудіо
    def creat_anime_sound(self):
        self.canva = CTkCanvas(self, width=890, height=500, bg="#310A31")
        self.canva.place(x=0, y=400)

        self.stolp = []

        x1 = 10
        w = 60

        # створюємо стовпчики
        for i in range(15):
            h = randint(20, 400)
            color = self.random_color()
            y1 = 440 - h

            st = self.canva.create_rectangle(
                x1, y1, x1 + w, 500,
                fill=color,
                outline=""
            )
            self.stolp.append(st)
            x1 += w + 5

        self.anime()

    # випадковий темний колір
    def random_color(self):
        r = randint(0, 120)
        g = randint(0, 120)
        b = randint(0, 120)
        return f'#{r:02X}{g:02X}{b:02X}'

    # анімація стовпчиків
    def anime(self):
        if self.recording or self.playing:
            x1 = 10
            w = 60

            for i in range(15):
                h = randint(20, 400)
                color = self.random_color()
                y1 = 440 - h

                self.canva.coords(self.stolp[i], x1, y1, x1 + w, 500)
                self.canva.itemconfig(self.stolp[i], fill=color)

                x1 += w + 5

        self.after(150, self.anime)

    # запис + відтворення мінусовки
    def do_record(self):
        if not self.recording:
            sd.stop()
            self.playing = False
            self.recording = True

            self.btn_record.configure(text="Stop")
            self.lbl_info.configure(text="Recording... Press Stop when done")

            # завантаження мінусовки
            self.fs, self.minus = wavfile.read(self.minus)

            # зменшуємо гучність мінуса
            minus_play = (self.minus * 0.4).astype(self.minus.dtype)

            # запис + відтворення одночасно
            self.recording_file = sd.playrec(
                minus_play,
                samplerate=self.fs,
                channels=1
            )

        else:
            # зупинка запису
            sd.stop()
            self.recording = False

            self.btn_record.configure(text="Start")
            self.lbl_info.configure(text="Processing and saving...")

            self.save_file()

    # збереження та мікс звуку
    def save_file(self):
        mic = self.recording_file.astype(np.float32)
        minus_cut = self.minus[:len(mic)].astype(np.float32)

        # мікс голос + мінус
        mixed = minus_cut + mic
        mixed /= np.max(np.abs(mixed))  # нормалізація

        # збереження файлу
        record = os.path.join(
            record_path,
            f"record_{randint(1000,9999)}.wav"
        )

        wavfile.write(record, self.fs, (mixed * 32767).astype(np.int16))

        # відтворення результату
        sd.play(mixed, samplerate=self.fs)
        self.playing = True