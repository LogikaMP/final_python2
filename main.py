# Імпортувати бібліотеку pygame (ігровий рушій)
import pygame
# Імпортувати всі налаштування (ширина, висота, кольори, шляхи тощо)
from settings import*
# Імпортувати клас кнопки
from buttons import Button
# Імпортувати функцію генерації кнопок з випадковими літерами
from random_letters import generat_btn
# Імпортувати генератор випадкових чисел
from random import randint
'''Імпортувати класи гравця і ворога'''
from player import Player, Enemy
'''Імпортувати Меню з файлу меню'''
from menu import Menu
# Запустити ініціалізацію pygame
pygame.init()

# Створити функцію для старту гри
# Змінити стан гри на "гра"
def start_game():
    global game_part
    game_part = "game"
    restart()

# Створити функцію для перезапуску гри
# Дозволити змінювати глобальні змінні
# Перевести гру в стан "гра"
# Згенерувати новий набір кнопок (3–15 випадкових)
# Створити нового гравця на стартовій позиції
# Створити нового ворога на початковій позиції
def restart():
    global game_part, btns, player, enemy
    game_part = "game"
    '''5.виправити генерацію букв за рівнем гри
    зі списка LEVELS беремо рівень номер що зберігається в меню menu_ui.level'''
    btns = generat_btn(LEVELS[menu_ui.level])
    '''5.як фон увімкнений(перервіряємо прапор з меню fon_music)
    завантажити фонову музику зі списку FON_MUSICS за нмоером menu_ui.music
    налашутвати гучність - 0.5, включити на програвання -1'''
    if menu_ui.fon_music:
        pygame.mixer.music.load(FON_MUSICS[menu_ui.music])
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)
    
    player = Player(100, HEIGHT//2+75, 50, 50, 5, PLAYERS)
    enemy = Enemy(10, HEIGHT//2+75, 50, 50, 3, ENEMYS)

'''4.Створити функцію обробник для зміни на вікно меню
міняємо зміну game_part'''
def open_menu():
    global game_part
    game_part = "menu"

    ...
'''4.Створити функцію обробник для зміни на вікно старт
міняємо зміну game_part'''
def back():
    global game_part
    game_part = "start"
    ...
# Створити головне вікно гри з заданими розмірами
# Встановити назву вікна
# Завантажити фон з папки зображень
# Масштабувати фон під розмір вікна
window = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("key train")
fon = pygame.image.load(FON)
fon = pygame.transform.scale(fon,(WIDTH,HEIGHT))
# Створити таймер гри
clock = pygame.time.Clock()


# Створити гравця
# Створити ворога
start_btn = Button(200,200,200,60,BLUE,
                   "Start",WHITE,command = start_game)
'''4.Створити кнопку для переходу в меню
х,у = 200, 300, ширина,висота - 200 60
кольри -BLUE,  WHITE, текст - Menu
команда - open_menu'''
menu_bt = Button(200,300,200,60,BLUE,
                     "Menu",WHITE,command = open_menu)

'''4.Створити меню
координати - 200 50, розмір 200, 85'''
menu_ui = Menu(200,50,200,85)
'''4.Створити кнопку для переходу назад у старт з гри
х,у = 20, 20, ширина,висота - 100 30
кольри -BLUE,  WHITE, текст - Back
команда - back'''
start_returt = Button(20,20,100,30,BLUE,
                     "Back",WHITE,command = back)
# Створити кнопку кінця гри
# Створити кнопку перезапуску гри
btn_end = Button(200,150,200, 80,RED,
                   "EXIT",WHITE, command = quit)
btn_restart = Button(200,270,200, 100,BLUE,
                   "RESTART",WHITE, command = restart)
btn_menu = Button(200,270,200, 100,BLUE,
                   "MENU",WHITE, command = open_menu)



'''1.створити глобальні змінні для гравця, ворога, та кнопок'''
player=None
enemy=None
btns=[]
# Увімкнути головний цикл гри
# Встановити початковий стан меню
# Змінна, яка визначає перемогу або поразку
run = True
game_part = "start"
end_game = "win"

# Почати нескінченний цикл гри
# Малювати фон на кожному кадрі
# Перевіряти всі події (клавіатура, миша, закриття)
# Якщо натиснули закрити вікно — завершити гру
# Якщо є кнопки на екрані
# Якщо користувач натиснув правильну клавішу — видалити кнопку
while run :
    window.blit(fon,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        '''1.Перевірити чи натсинута клавіша , триває гра та ще є букви-кнопки'''
        if event.type == pygame.KEYDOWN and game_part == "game" and btns:
            '''1.отримати назву кнокпи натиснутої - event.unicode'''
            btn_name = event.unicode
            '''1. Перевірити назву кнокпи та кнопки букви-btns[0].letter'''
            if btn_name == btns[0].letter:
                '''1.якщо вірна видалити її зі списку btns'''
                del btns[0]
          
                



# Якщо гра в меню
# Намалювати кнопку старту
# Перевірити, чи натиснули кнопку старту
    if game_part== "start":
        start_btn.draw(window)
        start_btn.is_clicked()
        menu_bt.draw(window)
        menu_bt.is_clicked()
        '''6.відобразити та перевірити клік по кнопці меню'''
       
        
# Якщо гра активна
# Намалювати всі кнопки літер
# Оновити гравця (рух, взаємодія)
# Оновити ворога
# Якщо гравець зіткнувся з ворогом
# Перейти в екран кінця гри
# Позначити програш
# Якщо гравець дійшов до кінця рівня
# Перейти в екран кінця гри
# Позначити перемогу
    if game_part == "game":
        '''6.Відобразити ат перевірити по кнопці назад до старту'''
       
        
        for btn in btns:
            btn.draw(window)

        player.update(window, btns)
        enemy.update(window)
        '''2. Перевірка на вигращ - якщо кнопок-букв не залишилось
        змінити game_part та end_game'''
        if len(btns) == 0:
            end_game = "win"
            game_part = "end"
        '''2. Перевірка на програш - якщо ДІГНАВ ВОРОГО
        змінити game_part та end_game'''
        if player.rect.colliderect(enemy.rect):
            end_game = "lose"
            game_part = "end"
        


# Якщо гра закінчилась
# Якщо гравець виграв
# Показати текст перемоги
# Якщо програв
# Показати текст поразки
# Оновити текст кнопки результату
# Намалювати кнопку результату
# Намалювати кнопку рестарту
# Перевірити натискання рестарту
    if game_part == "end":
        if end_game == "win":
            text = "YOU WIN!"
        else:
            text = "YOU LOSE!"
        btn_end.add_text(text)
        btn_end.draw(window)
        btn_restart.draw(window)
        btn_restart.is_clicked()
    '''6.яКЩО ЗАРАЗ МЕНЮ: онвоити меню
    якщо прапор в меню menu_ui.back_start- 
    змінити змінну game_part та прапор menu_ui.back_start'''
    if game_part == "menu":
        menu_ui.update(window)
        if menu_ui.back_start:
            game_part = "start"
            menu_ui.back_start = False

# Оновити екран (показати всі зміни)
# Обмежити FPS гри
    pygame.display.flip()
    clock.tick(FPS)