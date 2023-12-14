import pygame.image
pygame.mixer.pre_init(44100, -16, 1, 512)

pygame.init()

game = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
but_sound = pygame.mixer.Sound("меню,кнопки/кнопка.wav")
start_sound = pygame.mixer.Sound("level_2/вход.wav")
hallway_sound = pygame.mixer.Sound("level_2/коридор.wav")
kitchen_sound = pygame.mixer.Sound("level_2/кухня.wav")
room_sound = pygame.mixer.Sound("level_2/конец.wav")
door_sound_yes = pygame.mixer.Sound("level_2/ага.wav")
door_sound_no = pygame.mixer.Sound("level_2/не-а.wav")


def print_text(message, x, y, font_size=30, font_color=(255, 255, 255), font_type="меню,кнопки/a ConceptoTitulRough.ttf"):
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(message, True, font_color)
    game.blit(text, (x, y))


class Button:
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


class Picture_button():
    def draw(self, x, y, message, size=30, action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x < mouse[0] < x + 400 and y < mouse[1] < y + 400:
            game.blit(pygame.image.load("меню,кнопки/кнопкаlight_прямоугольник.png"), (x, y))
            print_text(message, x + 50, y + 50, size)
            pygame.display.update()
            if click[0] == 1:
                but_sound.play()
                return action
        else:
            game.blit(pygame.image.load("меню,кнопки/кнопка_прямоугольник.png"), (x, y))
            print_text(message, x + 50, y + 50, size)
            pygame.display.update()
        return False


button_exit = Button()
button_choise = Picture_button


class Communalka():
    def room(self, win):
        pass  # игрок умер

    def room_gg(self, win):  # комната игрока
        game.blit(pygame.image.load("level_2/комнатаГГ.jpg"), (-100, 0))
        while win:
            for event in pygame.event.get():
                win = button_exit.draw(750, 800, 800, 850)
                if event.type == pygame.QUIT:
                    win = False
                print_text('"Наконец-то от меня отстал этот странный тип.', 100, 650)
                print_text('Комнатка жуткая, но ночевать больше всё равно негде"', 300, 700)
                pygame.display.update()
                a = button_choise.draw(self, 1000, 750, "Разложить вещи", 30, 'behind_door')
                if a:
                    while win:
                        for event in pygame.event.get():
                            win = button_exit.draw(750, 800, 800, 850)
                            if event.type == pygame.QUIT:
                                win = False
                            game.blit(pygame.image.load("level_2/комнатаГГ_вещи.png"), (-100, 0))
                            print_text('"День был очень утомительным"', 300, 700)
                            pygame.display.update()
                            c = button_choise.draw(self, 300, 750, "Лечь спать", 30, True)
                            if c:
                                while c:
                                    game.blit(pygame.image.load("level_2/потолок.jpg"), (0, 0))
                                    pygame.display.update()
                                    pygame.time.delay(300)
                                    game.blit(pygame.image.load("level_2/потолок.jpg"), (0, 0))
                                    pygame.display.update()

    def behind_door(self):  # у двери
         pass

    def kitchen(self, win):  # кухня
        kitchen_sound.play()
        game.blit(pygame.image.load("level_2/кухня.png"), (-50, -50))
        game.blit(pygame.image.load("level_2/Геннадий_2.0.png"), (800, 150))
        pygame.display.update()
        pygame.time.delay(11000)
        while win:
            for event in pygame.event.get():
                win = button_exit.draw(750, 800, 800, 850)
                if event.type == pygame.QUIT:
                    win = False
                print_text('Так-с, ну плита есть, газ есть. Ах, дурная голова!', 100, 650)
                print_text('Чайник в своей комнате забыл. Пойдем со мной, я тебе её покажу.', 300, 700)
                pygame.display.update()
                a = button_choise.draw(self, 1000, 750, "За чайником", 30, 'behind_door')
                if a:
                    self.behind_door()
                    win = False
                b = button_choise.draw(self, 300, 750, "Где моя комната?", 30, 'room_gg')
                if b:
                    self.room_gg(True)
                    win = False

    def hallway(self, win):  # коридор
        hallway_sound.play()
        game.blit(pygame.image.load("level_2/коридор.jpg"), (-100, -100))
        game.blit(pygame.image.load("level_2/Геннадий_2.0.png"), (800, 150))
        pygame.display.update()
        pygame.time.delay(9000)
        while win:
            for event in pygame.event.get():
                win = button_exit.draw(750, 800, 800, 850)
                if event.type == pygame.QUIT:
                    win = False
                print_text('Ну и погодка! Вы там не замезли? Может чаю?', 100, 650)
                print_text('Я настаиваю!', 300, 700)
                pygame.display.update()
                a = button_choise.draw(self, 1000, 750, "Пить чай", 60, 'kitchen')
                if a:
                    self.kitchen(True)
                    win = False
                b = button_choise.draw(self, 300, 750, "Сначала моя комната", 25, 'room_gg')
                if b:
                    self.room_gg(True)
                    win = False

    def start_level(self, win):  # вход в квартиру
        start_sound.play()
        game.blit(pygame.image.load("level_2/вход.png"), (-100, -100))
        game.blit(pygame.image.load("level_2/Геннадий_2.0.png"), (800, 150))
        pygame.display.update()
        pygame.time.delay(10000)
        print_text('Добрый вечер. Ах, да! Вы к нам из столицы, хотите снять у нас комнату!', 100, 650)
        print_text('                                          Я Геннадий. Проходите!', 300, 700)
        pygame.display.update()
        while win:
            for event in pygame.event.get():
                win = button_exit.draw(750, 800, 800, 850)
                if event.type == pygame.QUIT:
                    win = False
                a = button_choise.draw(self, 300, 750, "  Войти", 60, 'hallway')
                if a:
                    self.hallway(True)
                    win = False
        game.blit(pygame.image.load("меню,кнопки/меню.jpg"), (0, -80))
        pygame.display.update()
