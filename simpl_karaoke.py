from customtkinter import CTk, CTkButton, CTkLabel, CTkCanvas
import sounddevice as sd
from scipy.io import wavfile
import os
import numpy as np
from random import randint

minus_path = os.path.join(os.path.dirname(__file__), "DREVO.wav")
record_path = os.path.join(os.path.dirname(__file__), "DREVO-record.wav")

class App(CTk):
    def __init__(self):
        super().__init__(fg_color="#310A31")
        self.geometry("600x500")
        self.title("Simple Karaoke")

        self.recording = False
        self.playing = False

        self.creat_anime_sound()
        
        lbl = CTkLabel(self, text="Simple Karaoke", text_color="#BF9BC6",
                       font=("Arial", 40))
        lbl.pack(pady=30)

        self.btn_record = CTkButton(self, text="Start", width=200, height=100,
                                    fg_color="#C52EA7", corner_radius=50,
                                    border_color="#BC8CB7", border_width=10,
                                    command=self.do_record)
        self.btn_record.bind("<Button-3>", self.stop_all)
        self.btn_record.pack()

        self.lbl_info = CTkLabel(self, text="Start record + minus", text_color="#DABBD5",
                                 font=("Arial", 16))
        self.lbl_info.pack()
        lbl2 =  CTkLabel(self, text="Left click stop all", text_color="#DABBD5",
                                 font=("Arial", 16))
        lbl2.pack()

    def stop_all(self, e):
        sd.stop()
        self.playing = False
        self.recording = False
        self.btn_record.configure(text="Start")
        self.lbl_info.configure(text="Processing and saving...")

    def creat_anime_sound(self):
        self.canva = CTkCanvas(self, width=890, height=440, bg="#310A31")
        self.canva.place(x=0, y=300)
        self.stolp = []

        x1 = 10        # початкова горизонтальна позиція
        w = 60         # ширина кожного стовпчика
        for i in range(15):
            h = randint(20, 400)  # висота стовпчика
            # Генеруємо яскравий випадковий колір
            color = self.random_color()
            y1 = 440 - h  # ставимо на “дно” канвасу
            st = self.canva.create_rectangle(x1, y1, x1 + w, 440, fill=color, outline="")
            self.stolp.append(st)
            x1 += w + 5  # крок по горизонталі

        self.anime()

    def random_color(self):
        r = randint(150, 255)
        g = randint(150, 255)
        b = randint(150, 255)
        return f'#{r:02X}{g:02X}{b:02X}'
    
    def anime(self):
        if self.recording or self.playing:
            x1 = 10        # початкова горизонтальна позиція
            w = 60         # ширина кожного стовпчика
            for i in range(15):
                h = randint(20, 400)  # висота стовпчика
                # Генеруємо яскравий випадковий колір
                color = self.random_color()
                y1 = 440 - h  # ставимо на “дно” канвасу
                self.canva.coords(self.stolp[i],x1,y1,x1+w,440)
                self.canva.itemconfig(self.stolp[i], fill=color)
                x1 += w + 5  # крок по горизонталі
        self.after(150, self.anime)


    def do_record(self):
        if not self.recording:
            sd.stop()
            self.playing = False
            self.recording = True
            self.btn_record.configure(text="Stop")
            self.lbl_info.configure(text="Recording... Press Stop when done")

            # 1. Завантажуємо мінусовку
            self.fs, self.minus = wavfile.read(minus_path)

            # 2. Зменшуємо гучність мінусовки для запису (щоб голос був чутний)
            minus_play = (self.minus * 0.4).astype(self.minus.dtype)

            # 3. Одночасне відтворення мінусовки та запис мікрофона
            self.recording_file = sd.playrec(minus_play, samplerate=self.fs, channels=1)
        else:
            # Stop record
            sd.stop()
            self.recording = False
            self.btn_record.configure(text="Start")
            self.lbl_info.configure(text="Processing and saving...")
            self.save_file()

    def save_file(self):
        # Мінусовка оригінальна (для кращого звучання)
        mic = self.recording_file.astype(np.float32)
        minus_cut = self.minus[:len(mic)].astype(np.float32)

        # 4. Змішування: мінусовка + мікрофон
        mixed = minus_cut + mic
        mixed /= np.max(np.abs(mixed))  # нормалізація

        # 5. Збереження та відтворення
        wavfile.write(record_path, self.fs, (mixed*32767).astype(np.int16))
        sd.play(mixed, samplerate=self.fs)
        self.playing = True


App().mainloop()