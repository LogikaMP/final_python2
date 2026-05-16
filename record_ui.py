from customtkinter import CTkButton, CTkLabel, CTkFrame, CTkScrollableFrame
from settings import *
import sounddevice as sd
from scipy.io import wavfile
import os


# ================= МЕНЮ =================
'''НОВЕ:Напиши клас вікна записів караоке'''
class RecordsFrame(CTkFrame):
    def __init__(self, app):
        super().__init__(app, fg_color="transparent")

        self.app = app

        # НОВЕ: Додай кнопку 🔙 кнопка назад (верхній правий кут) 
        # текст "⬅️"б розмір 60 на 40 колір "#3c80bc" та "#061076"
        # команда self.app.back 
        # розаташування place(relx=1.0, x=-10, y=10, anchor="ne")
        CTkButton(self,width=60,height=40,bg_color="#3c80bc",text_color="#061076",text="⬅️",
        command=self.app.back).place(relx=1.0, x=-10, y=10, anchor="ne")

        self.pack(fill="both", expand=True) 
        # заголовок - лейбл текст "Записи каракоке:", колір "#b89bc6", шрифт 36 
        # розташуй pack(pady=(40, 10))
        CTkLabel(self,text="Записи каракоке",text_color="#b89bc6",font=("Arial",36)).pack(pady=(40, 10))
        #НОВЕ: створи вікно скролінгу для відображення записів віджет CTkScrollableFrame 
        # фон "transparent" розташуй pack(fill="both", expand=True) 
        self.scroll=CTkScrollableFrame(self,fg_color="transparent")
        self.scroll.pack(fill="both", expand=True)


        #НОВЕ:викли метод додавання лейблів та кнопок пісень-записів
        self.add_records()
        #НОВЕ: властивість прапор грає чи ні
        self.play_no=False
        #НОВЕ:властивість з номером попереднього програваємого запису = 0
        self.before=0
    #НОВЕ: Метод додати записи
    def add_records(self):
        #НОВЕ: спершу видали усі віджети зі скролінгу 
        # отримати віджети -self.scroll.winfo_children()
        #  видалити widget.destroy()
        for widget in self.scroll.winfo_children():
            widget.destroy()

        #НОВЕ: отримати усі записи зі папки записів черх ос os.listdir
        file=os.listdir(record_path)
        #НОВЕ: лічильник для номеру запису = 0
        i = 0
        #НОВЕ: список записів порожній
        self.record=[]
        #НОВЕ: цикл переребору записів файлів
        for ap in file:
            #НОВЕ: створити лейбл кріпимо на скролінг текст = назва файлу 
            # колір"#b89bc6", шрифт 36
            L=CTkLabel(self.scroll,text=ap,text_color="#b89bc6",font=("Arial",36))

            #НОВЕ: кріпимо як сітку (grid) ряд = і, колонка 0, відступи 50, 10
            L.grid(row=i,column= 0,padx= 50,pady = 10)
            #НОВЕ: додати у спсиок
            self.record.append(L)
            #НОВЕ: додати кнопку грати до цього запису на скролінг 
            # текст "🔊", розмір 30 на 30, колір "#3c80bc" 
            # команада lambda file=file, i = i:self.play(file,i) 
            # кріпимо - ряд = і, колонка 2 вітсупи 20 10
            CTkButton(self.scroll,text="🔊",width=30,height=30,fg_color="#3c80bc",command=lambda ap=ap,
             i = i:self.play(ap,i)).grid( row=i,column=1,padx=20,pady=10)

            #НОВЕ: додати кнопку грати до цього запису на скролінг 
            # текст ="🗑️", розмір 30 на 30, колір "#3c80bc" 
            # команада lambda file=file : self.del_sound(file)
            # кріпимо - ряд = і, колонка 2 вітсупи 20 10
            CTkButton(self.scroll,text="🗑️",width=30,height=30,fg_color="#3c80bc",command=lambda ap=ap,
            :self.del_sound(ap)).grid( row=i,column=2,padx=20,pady=10)
            #НОВЕ: збільшити лічильник і
            i += 1  


    #НОВЕ: метод видалити пісню       
    def del_sound(self,sound):
        #НОВЕ: видаляємо файл з папки метод ос remove
        os.remove(record_path+sound)
        #НОВЕ: скинути лічильник попредньої псні на 0
        self.before = 0
        #НОВЕ: викликати метод доати пісні для онволення списку записів
        self.add_records()
        
    #НОВЕ: Метод грати     
    def play(self, sound, i):
        #НОВЕ: якщо ве грає - зупинити 
        sd.stop()
        #НОВЕ:прапор грає включити
    
        #НОВЕ:якщо в списку пісень більше ніж 2
        #НОВЕ:змінити колір попереднього віджета лейбла пісні на text_color= "#b89bc6"
        if len(self.record)>=2:
            self.record[self.before].configure(text_color= "#b89bc6")

        #НОВЕ:змінити колір віджета і лейбла пісні на text_color= "#3c80bc"
        self.record[i].configure(text_color= "#3c80bc")
        #НОВЕ: зампятати обрану пісню 
        self.before=i
        
        #НОВЕ: читаємо файд
        f,s=wavfile.read(record_path+sound)
        #НОВЕ:граємо файл
        sd.play(s,f)
    


    