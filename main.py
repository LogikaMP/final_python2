import customtkinter as ctk
from settinhs import*
from menu import Menu
from train import GameFrame

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.theme = 0
        self.temu = themes[self.theme]
        self.level = 0
        self.music = settings_data["music"][0]
        self.volume = 0
        self.geometry("600x500")
        self.title("Typing trainer")
        self.configure(fg_color = self.temu["bg"])
        self.menu = None
        self.game = None
        self.frame = ctk.CTkFrame(self,fg_color=self.temu["frame"])
        self.frame.pack(fill="both",expand=True, padx=15, pady=15)
        ctk.CTkLabel(self.frame,text= "Вітаємо в тренажері друку",text_color=self.temu["text"]
                     ,font=("Arial",36)).pack(pady = (100, 20))
        ctk.CTkLabel(self.frame,text= "Перевір свою швидкість друку",text_color=self.temu["text"]
                     ,font=("Arial",16)).pack(pady = 10)
        ctk.CTkButton(self.frame,text="Старт",text_color=self.temu["text"]
                      ,fg_color=self.temu["button"],corner_radius=25,
                      font=("Arial",16), border_color=self.temu["button_hover"],
                       border_width=5,
                      command=self.start).pack(pady = 20)
        ctk.CTkButton(self.frame,text="Налаштування",text_color=self.temu["text"]
                      ,fg_color=self.temu["button"],corner_radius=25,
                      font=("Arial",16), border_color=self.temu["button_hover"],
                      border_width=5,
                      command=self.setting).pack(pady = 20)
        
    def start(self):
        self.frame.pack_forget()
        self.game =GameFrame(self)
    def setting(self):
        self.frame.pack_forget()
        self.menu = Menu(self)

    def back(self):
        if self.game:
            self.game.destroy()
            self.frame.pack(fill="both",expand=True, padx=15, pady=15)
        if self.menu:
            self.menu.destroy()
            self.frame.pack(fill="both",expand=True, padx=15, pady=15)
App().mainloop()
            



        
    