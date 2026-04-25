'''UI кнопки – елементи керування'''

'''UI кнопки – елементи керування'''
import pygame
class Sprite:
    def __init__(self,x=10,y=10,w=50,h=50,speed=0,image=None,color=(200,0,0)):
            self.image = image
            self.color = color
            self.rect = pygame.Rect(x,y,w,h)
            self.speed = speed
            self.load_img()
    def draw(self,window):
         if self.image:
              window.blit(self.image,self.rect)
         else:
              pygame.draw.rect(window,self.color,self.rect)
    def move(self,window):
         key = pygame.key.get_pressed()
         if key[pygame.K_w] and self.rect.y >= self.speed:
              self.rect.y -= self.speed
         if key[pygame.K_s] and self.rect.bottom <= window.get_height() - self.speed:
              self.rect.y += self.speed
         if key[pygame.K_a] and self.rect.x >= self.speed:
              self.rect.x -= self.speed
         if key[pygame.K_d] and self.rect.right <= window.get_wigth() - self.speed:
              self.rect.x += self.speed
    def load_img(self):
         if self.image:
              self.image = pygame.image.load(self.image)
              self.image = pygame.transform.scale(self.image,(self.rect.w, self.rect.h))

class Button(Sprite):  # Створюємо клас кнопки, який наслідує властивості класу Sprite
     
     def __init__(self, x, y, w, h, color, text, color_text, command,image = None):
          # Конструктор класу. Виконується при створенні об'єкта кнопки

          # Викликаємо конструктор батьківського класу Sprite і передаємо координати, розміри та колір
          super().__init__(x,y,w,h,0,None,color)
          self.color_text = color_text
          # Зберігаємо колір тексту кнопки
          self.command = command
          self.text = text
          # Зберігаємо функцію, яка виконається при натисканні кнопки
          if image:
               self.image = pygame.image.load(image)
               self.image = pygame.transform.scale(self.image,(w,h))
          elif text:
               self.add_text(text)
               # Викликаємо метод створення тексту на кнопці
          self.was_pressed = False
          # Прапорець, що показує чи була кнопка натиснута раніше


     def add_text(self, text):  
          # Метод створення та розміщення тексту на кнопці

          # h = 0.45, w = 0.55 (коефіцієнти підбору розміру шрифту)
          size_h = self.rect.h // 0.45
          # Розраховуємо розмір шрифту від висоти кнопки
          size_w = self.rect.w // (0.55 * len(text))
          # Розраховуємо розмір шрифту від ширини кнопки та довжини тексту
          font_size = min(size_h, size_w)
          # Обираємо менше значення, щоб текст точно помістився
          font = pygame.font.Font(None, int(font_size))
          # Створюємо шрифт потрібного розміру
          self.text = font.render(text, True, self.color_text)
          # Створюємо зображення тексту
          self.text_x = (self.rect.w - self.text.get_width()) // 2 + self.rect.x
          # Обчислюємо координату X для центрування тексту по горизонталі
          self.text_y = (self.rect.h - self.text.get_height()) // 2 + self.rect.y
          # Обчислюємо координату Y для центрування тексту по вертикалі


     def draw(self, surface):
          if self.image:
               surface.blit(self.image,self.rect)
          else:  
               # Метод відмалювання кнопки на екрані
               super().draw(surface)
               pygame.draw.rect(surface,(0,0,0),self.rect,width=5)
               # Малюємо саму кнопку через метод батьківського класу
               if self.text:
                    surface.blit(self.text, (self.text_x, self.text_y))
               # Малюємо текст поверх кнопки
          
     def is_clicked(self):  
          # Метод перевіряє чи натиснута кнопка

          if self.command:  
               # Перевіряємо чи є функція для виконання
               click = pygame.mouse.get_pressed()[0]
               # Перевіряємо чи натиснута ліва кнопка миші
               pos = pygame.mouse.get_pos()
               # Отримуємо поточну позицію курсора
               if  click and self.rect.collidepoint(pos) and not self.was_pressed:
                    # Якщо кнопка миші натиснута, курсор знаходиться на кнопці
                    # і попередній стан не був натисканням
                    self.command()
                    # Виконуємо функцію кнопки
               self.was_pressed = click
               # Запам’ятовуємо стан кнопки миші, щоб не викликати функцію багато разів