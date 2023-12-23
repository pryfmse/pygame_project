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


def print_text(message, x, y, font_size=30, font_color=(255, 255, 255),
               font_type="меню,кнопки/a ConceptoTitulRough.ttf"):
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(message, True, font_color)
    game.blit(text, (x, y))


class Button():
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
    def __init__(self, active="меню,кнопки/кнопкаlight_прямоугольник.png",
                 inactive="меню,кнопки/кнопка_прямоугольник.png", area=400):
        self.active = active
        self.inactive = inactive
        self.area = area

    def draw(self, x, y, message, size=30, action=True):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x < mouse[0] < x + self.area and y < mouse[1] < y + self.area:
            game.blit(pygame.image.load(self.active), (x, y))
            print_text(message, x + 50, y + 50, size)
            pygame.display.update()
            if click[0] == 1:
                but_sound.play()
                return action
        else:
            game.blit(pygame.image.load(self.inactive), (x, y))
            print_text(message, x + 50, y + 50, size)
            pygame.display.update()
        return False


class Results(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.speed = 100
        self.image = pygame.image.load('level_1/game_lab/результаты.jpg')
        self.rect = self.image.get_rect()
        self.rect.x = -1000
        self.rect.y = 200

    def update(self):
        if self.rect.x < 400:
            self.rect.x += self.speed


button_exit = Button()
button_choise = Picture_button()
button_replace = Picture_button('level_2/game_sheep/кнопка_заново_светлая.png',
                                'level_2/game_sheep/кнопка_заново_темная.png', 150)


class Communalka():
    def game_sheep(self, win):
        field = [
            ['0', '5', '0', '0', ' '],
            ['0', '2', '9', '0', '0'],
            ['2', '2', '0', '5', '0'],
            ['5', '0', '0', '01', ' ']
        ]
        x, y = 3, 3
        end = False
        start = pygame.time.get_ticks()
        now = []
        sprite = pygame.sprite.Group()
        replace = button_replace.draw(1300, 20, "")
        res = Results()
        sprite.add(res)
        while win:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    win = False

                if event.type == pygame.KEYDOWN and not end:
                    if event.key == pygame.K_LEFT:
                        if y != 0:
                            if field[x][y - 1] == '0':
                                field[x][y - 1] = '01'
                                field[x][y] = field[x][y][:-1]
                                x, y = x, y - 1
                            elif field[x][y - 1] == '5':
                                field[x][y - 1] = '51'
                                field[x][y] = field[x][y][:-1]
                                x, y = x, y - 1
                            elif field[x][y - 1][-1] == '2' and y > 1 and (field[x][y - 2] == '0'
                                                                           or field[x][y - 2] == '5'):
                                field[x][y - 1] = '01'
                                field[x][y - 2] = '2' if field[x][y - 2] == '0' else '52'
                                field[x][y] = field[x][y][:-1]
                                x, y = x, y - 1
                    if event.key == pygame.K_RIGHT:
                        if not((x == 0 and y == 3) or (x == 3 and y == 3) or y == 4):
                            if field[x][y + 1] == '0':
                                field[x][y + 1] = '01'
                                field[x][y] = field[x][y][:-1]
                                x, y = x, y + 1
                            elif field[x][y + 1] == '5':
                                field[x][y + 1] = '51'
                                field[x][y] = field[x][y][:-1]
                                x, y = x, y + 1
                            elif field[x][y + 1][-1] == '2' and ((y < 3 and (x == 2 or x == 1)) or
                                                                 y < 2 and (x == 0 or x == 3)) and (
                                    field[x][y + 2] == '0' or field[x][y + 2] == '5'):
                                field[x][y + 1] = '01'
                                field[x][y + 2] = '2' if field[x][y + 2] == '0' else '52'
                                field[x][y] = field[x][y][:-1]
                                x, y = x, y + 1
                    if event.key == pygame.K_UP:
                        if x != 0:
                            if field[x - 1][y] == '0':
                                field[x - 1][y] = '01'
                                field[x][y] = field[x][y][:-1]
                                x, y = x - 1, y
                            elif field[x - 1][y] == '5':
                                field[x - 1][y] = '51'
                                field[x][y] = field[x][y][:-1]
                                x, y = x - 1, y
                            elif field[x - 1][y][-1] == '2' and x > 1 and (
                                    field[x - 2][y] == '0' or field[x - 2][y] == '5'):
                                field[x - 1][y] = '01'
                                field[x - 2][y] = '2' if field[x - 2][y] == '0' else '52'
                                field[x][y] = field[x][y][:-1]
                                x, y = x - 1, y
                    if event.key == pygame.K_DOWN:
                        if x < 3:
                            if field[x + 1][y] == '0':
                                field[x + 1][y] = '01'
                                field[x][y] = field[x][y][:-1]
                                x, y = x + 1, y
                            elif field[x + 1][y] == '5':
                                field[x + 1][y] = '51'
                                field[x][y] = field[x][y][:-1]
                                x, y = x + 1, y
                            elif field[x + 1][y][-1] == '2' and x < 2 and (
                                    field[x + 2][y] == '0' or field[x + 2][y] == '5'):
                                field[x + 1][y] = '01'
                                field[x + 2][y] = '2' if field[x + 2][y] == '0' else '52'
                                field[x][y] = field[x][y][:-1]
                                x, y = x + 1, y

            game.blit(pygame.image.load("level_2/потолок.jpg"), (0, 0))
            game.blit(pygame.image.load("level_2/game_sheep/облако.png"), (200, 0))

            if not end:
                print_text('Подвиньте овечек так,', 20, 20)
                print_text('чтобы каждая из них', 20, 60)
                print_text('оказалась на своем месте', 20, 100)
                for j in range(4):
                    for i in range(5):
                        if not(j == 0 and i == 4) and not(j == 3 and i == 4):
                            game.blit(pygame.image.load("level_2/game_sheep/клетка.png"), (450 + 130 * i, 200 + 130 * j))
                            if '5' in field[j][i]:
                                game.blit(pygame.image.load("level_2/game_sheep/крестик.png"),
                                          (450 + 130 * i + 50, 200 + 130 * j + 50))
                            if '9' in field[j][i]:
                                game.blit(pygame.image.load("level_2/game_sheep/камень.png"),
                                          (450 + 130 * i + 50, 200 + 130 * j + 50))
                            if '2' in field[j][i]:
                                game.blit(pygame.image.load("level_2/game_sheep/овечка.png"),
                                          (450 + 130 * i + 50, 200 + 130 * j + 50))
                            if '1' in field[j][i]:
                                game.blit(pygame.image.load("level_2/game_sheep/собака.png"),
                                          (450 + 130 * i + 50, 200 + 130 * j + 50))
            if replace:
                field = [
                    ['0', '5', '0', '0', ' '],
                    ['0', '2', '9', '0', '0'],
                    ['2', '2', '0', '5', '0'],
                    ['5', '0', '0', '01', ' ']
                ]
                x, y = 3, 3
                end = False
                start = pygame.time.get_ticks()

            if field[0][1] == '52' and field[2][3] == '52' and field[3][0] == '52' and not end:
                now = pygame.time.get_ticks()
                end = True

            if end:
                sprite.update()
                sprite.draw(game)

            if end and res.rect.x == 400:
                print_text('Вы выиграли!', 500, 300, 60)
                print_text(f'Время игры: {str((now - start) / 1000)} сек', 500, 400)

            win = button_exit.draw(750, 800, 800, 850)
            replace = button_replace.draw(1400, 20, "")

            pygame.display.flip()

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
                a = button_choise.draw(1000, 750, "Разложить вещи", 30, 'behind_door')
                if a:
                    while win:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                win = False
                        game.blit(pygame.image.load("level_2/комнатаГГ_вещи.png"), (-100, 0))
                        print_text('"День был очень утомительным"', 300, 700)
                        win = button_exit.draw(750, 800, 800, 850)
                        c = button_choise.draw(300, 750, "Лечь спать", 30, True)
                        pygame.display.flip()
                        if c:
                            self.game_sheep(True)
                            win = False

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
                a = button_choise.draw(1000, 750, "За чайником", 30, 'behind_door')
                if a:
                    self.behind_door()
                    win = False
                b = button_choise.draw(300, 750, "Где моя комната?", 30, 'room_gg')
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
                a = button_choise.draw(1000, 750, "Пить чай", 60, 'kitchen')
                if a:
                    self.kitchen(True)
                    win = False
                b = button_choise.draw(300, 750, "Сначала моя комната", 25, 'room_gg')
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
                a = button_choise.draw(300, 750, "  Войти", 60, 'hallway')
                if a:
                    self.hallway(True)
                    win = False
        game.blit(pygame.image.load("меню,кнопки/меню.jpg"), (0, -80))
        pygame.display.update()
