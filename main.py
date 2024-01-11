import pygame
from screeninfo import get_monitors

from level_2 import Communalka  # импортировать классы уровней
from level_1 import Hostel
from level_3 import Hotel

pygame.mixer.pre_init(44100, -16, 1, 512)

for m in get_monitors():  # получить параметры экрана
    print(m.width, m.height)

pygame.init()
pygame.mixer.music.load("меню,кнопки/фоновая.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.5)
game = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
clock = pygame.time.Clock()
but_sound = pygame.mixer.Sound("меню,кнопки/кнопка.wav")

pygame.display.set_caption('Геннадий_вход передает привет')


# функция, печатающая текст на экране
def print_text(message, x, y, font_size=30, font_color=(255, 255, 255),
               font_type="меню,кнопки/a ConceptoTitulRough.ttf"):
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(message, True, font_color)
    game.blit(text, (x, y))


start = pygame.image.load("меню,кнопки/обложка.jpg")
menu_img = pygame.image.load("меню,кнопки/меню.jpg")
game.blit(start, (0, -80))
print_text("Для перехода в меню нажмите любую клавишу", 450, 50)
pygame.display.update()
win = True


class Picture_button():  # класс кнопок с изображением
    def draw(self, inactive, active, x, y, message, action):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x < mouse[0] < x + 400 and y < mouse[1] < y + 400:
            game.blit(active, (x, y))
            print_text(message, x + 100, y + 350)
            pygame.display.update()
            if click[0] == 1:
                but_sound.play()
                if action == 1:
                    gaming1.entry(True)
                    pygame.time.delay(100)
                    menu(True)
                if action == 2:
                    gaming2.start_level(True)
                    pygame.time.delay(100)
                    menu(True)
                if action == 3:
                    gaming3.game_child(True)
                    pygame.time.delay(100)
                    menu(True)
        else:
            game.blit(inactive, (x, y))
            print_text(message, x + 100, y + 350)
            pygame.display.update()


class Button():  # класс кнопки выхода
    def __init__(self):
        self.inactive = pygame.image.load("меню,кнопки/кнопка_овал.png")
        self.active = pygame.image.load("меню,кнопки/кнопкаlight_овал.png")

    def draw(self, x, y, x_mes, y_mes):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x + 10 < mouse[0] < x + 175 and y < mouse[1] < y + 110:
            game.blit(self.active, (x, y))
            print_text("ВЫХОД", x_mes, y_mes)
            pygame.display.update()
            if click[0] == 1:
                but_sound.play()
                return False
        else:
            game.blit(self.inactive, (x, y))
            print_text("ВЫХОД", x_mes, y_mes)
            pygame.display.update()
        return True


button_exit = Button()
picture_botton = Picture_button()
gaming1 = Hostel()
gaming2 = Communalka()
gaming3 = Hotel()


def menu(win):  # функция меню
    pygame.mouse.set_visible(True)
    game.blit(menu_img, (0, -80))
    pygame.display.update()
    while win:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pass
        win = button_exit.draw(750, 800, 800, 850)
        picture_botton.draw(pygame.image.load("меню,кнопки/меню_коммуналка.jpg"),
                            pygame.image.load("меню,кнопки/меню_lightкоммуналка.png"), 600, 200,
                            "коммуналка", 2)
        picture_botton.draw(pygame.image.load("меню,кнопки/меню_общежитие.png"),
                            pygame.image.load("меню,кнопки/меню_lightобщежитие.png"), 100, 200, "общежитие", 1)
        picture_botton.draw(pygame.image.load("меню,кнопки/меню_гостиница.jpg"),
                            pygame.image.load("меню,кнопки/меню_lightгостиница.png"), 1100, 200, "гостиница", 3)


while win:  # приветственный экран
    pygame.mouse.set_visible(False)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            win = False
        if event.type == pygame.KEYDOWN:
            but_sound.play()
            menu(win)
            win = False

pygame.quit()
