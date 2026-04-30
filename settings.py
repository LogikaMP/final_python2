'''налаштування гри (розмір вікна, кольори, список нот)'''

# налаштування вікна
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 400

# налаштування клавіш для усіх рівнів
KEY_WIDTH = [75, 70, 60, 55]
KEY_HEIGHT =[ 120, 115, 110, 100]

#координати для відображення клавіш для усіх рівнів
X_KEY_START =[ 150, 125, 120, 95]

#швидкість рухуклавіш
SPEED = 1

WHITE = (255,255,255)
BLACK = (0,0,0)
GRAY = (200, 200, 200)
BLUE = (0, 0, 255)
FON = (24,30,103)

KEYS = {
    "a": "a6.mp3",
    "b": "b6.mp3",
    "d": "d6.mp3",
    "f": "f6.mp3",
    "g": "g6.mp3",
    "e": "e6.mp3",
    "c": "c6.mp3"
}
#шлях до папки зі звуками та зображеннями
sounds_path = "play_piano/assets/sounds/"
images_path = "play_piano/assets/images/"
#шляхи до зображень та звуків
FON_START = "fon.jpg"
WRONG_SOUND = "wrong.mp3"
MISSED_SOUND = "miss.mp3"
#списки з назвами файлів для фону, музики та кнопок
FON_SOUND = ["level1.mp3","level2.mp3","level3.mp3","level4.mp3","level5.mp3"]
LEVELS = ['fon_level0.png','fon_level1.png','fon_level2.png','fon_level3.png']
BTNS = ["start_1.png","start_2.png","start_3.png","start_4.png"]
#список з кількістю клавіш для кожного рівня
LEVELS_KEYS = [2,3,4,5,6]