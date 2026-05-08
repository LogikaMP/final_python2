from customtkinter import CTkButton, CTkLabel, CTkFrame
from settings import *


# ================= МЕНЮ =================
class MenuFrame(CTkFrame):
    def __init__(self, app):
        super().__init__(app, fg_color="transparent")

        self.app = app
        self.pack(fill="both", expand=True)

        # заголовок
        CTkLabel(
            self,
            text="Вітаємо в караоке!",
            text_color="#b89bc6",
            font=("Arial", 36)
        ).pack(pady=(40, 10))

        # підзаголовок
        CTkLabel(
            self,
            text="Обери пісню і почни співати",
            text_color="#dabbd5",
            font=("Arial", 24)
        ).pack(pady=(0, 20))

        # ================= СПИСОК ПІСЕНЬ =================
        songs = CTkFrame(self, fg_color="transparent")
        songs.pack()

        index = 0
        self.btn = []

        # 1 колонка
        for i in range(4):
            text = name_minus[index]

            b = CTkButton(
                songs,
                text=text,
                width=150,
                height=50,
                fg_color="#3c80bc",
                hover_color="#89216f",
                corner_radius=10
            )

            b.grid(column=0, row=i, padx=20, pady=10, sticky="ew")
            b.bind("<Button-1>", self.selekt)

            self.btn.append(b)
            index += 1

        # 2 колонка
        for i in range(4):
            text = name_minus[index]

            b = CTkButton(
                songs,
                text=text,
                width=150,
                height=50,
                fg_color="#3c80bc",
                hover_color="#89216f",
                corner_radius=10
            )

            b.grid(column=1, row=i, padx=20, pady=10, sticky="ew")
            b.bind("<Button-1>", self.selekt)

            self.btn.append(b)
            index += 1

        # інфо про вибір
        self.lbl = CTkLabel(
            self,
            text="Пісня не обрана",
            text_color="#dabbd5",
            font=("Arial", 20)
        )
        self.lbl.pack()

        # кнопка старту
        CTkButton(
            self,
            text="Почати",
            command=self.app.open_karaoke
        ).pack(side="left", expand=True)

        '''НОВЕ: створи кнопку для переходу у вікно записів
        текст - Записи
         команда - self.app.open_record 
         розташування - pack(side="left", expand=True)'''
        CTkButton(
            self,
            text="Записи",
            command=self.app.open_record
        ).pack(side="left", expand=True)
       
    # ================= ВИБІР ПІСНІ =================
    def selekt(self, event):
        btn = event.widget.master
        name = btn.cget("text")

        # оновлення тексту (з переносом)
        self.lbl.configure(text=f"Пісня:\n{name}")

        i = name_minus.index(name)

        # скидання старого вибору
        self.btn[self.app.song].configure(fg_color="#3c80bc")

        # новий вибір
        self.app.song = i
        self.btn[i].configure(fg_color="#bf9bc6")