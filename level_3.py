import pygame

pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()

game = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
but_sound = pygame.mixer.Sound("меню,кнопки/кнопка.wav")
fall_sound = pygame.mixer.Sound("level_3/упало.wav")
scared_sound = pygame.mixer.Sound("level_3/испуг.wav")
people_sound = pygame.mixer.Sound("level_3/кто-то.wav")


def print_text(message, x, y, font_size=30, font_color=(255, 255, 255),
               font_type="меню,кнопки/a ConceptoTitulRough.ttf"):
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
button_choise = Picture_button()
all_sprites = pygame.sprite.Group()
barrier_group = pygame.sprite.Group()
wall_group = pygame.sprite.Group()


class Hotel():
    def end(self, win):
        people_sound.play()
        while win:
            game.blit(pygame.image.load("level_3/подвал2.png"), (0, 0))
            pygame.display.update()
            pygame.time.delay(1000)
            game.blit(pygame.image.load("level_3/подвал3.png"), (0, 0))
            pygame.display.update()
            pygame.time.delay(1000)
            game.blit(pygame.image.load("level_3/люди.jpg"), (0, 0))
            pygame.display.update()
            pygame.time.delay(1000)
            win = False

    def basement(self, win):
        scared_sound.play()
        while win:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    win = False
            game.blit(pygame.image.load("level_3/подвал.png"), (0, 0))
            win = button_exit.draw(750, 800, 800, 850)
            print_text('Мне нельзя с тобой разговаривать, иначе они узнают', 100, 50)
            print_text('Скажу лишь, что тебе срочно нужно бежать, они тебя убьют!', 300, 100)
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            game.blit(pygame.image.load("level_1/курсор.png"), mouse)
            pygame.mouse.set_visible(False)
            if click[0] == 1:
                self.end(True)
                win = False

            pygame.display.update()

    def hall3(self, win):
        while win:
            while win:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        win = False
                game.blit(pygame.image.load("level_3/холл2.png"), (0, 0))
                win = button_exit.draw(750, 800, 800, 850)
                print_text('Постой! Ты кто?', 300, 700)
                mouse = pygame.mouse.get_pos()
                click = pygame.mouse.get_pressed()
                if 1050 < mouse[0] < 1150 and 550 < mouse[1] < 700:
                    game.blit(pygame.image.load("level_1/курсор.png"), mouse)
                    pygame.mouse.set_visible(False)
                    if click[0] == 1:
                        pygame.mouse.set_visible(True)
                        self.basement(True)
                        win = False
                else:
                    pygame.mouse.set_visible(True)

                pygame.display.update()

    def computer2(self, win):
        text = 'Что это значит? Меня тут кто-то ждал?'
        ok = False
        while win:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    win = False
            game.blit(pygame.image.load("level_3/компьютер2.png"), (0, 0))
            win = button_exit.draw(750, 800, 800, 850)
            print_text(text, 300, 700)
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            if 450 < mouse[0] < 1200 and 100 < mouse[1] < 600:
                game.blit(pygame.image.load("level_1/курсор.png"), mouse)
                pygame.mouse.set_visible(False)
                if click[0] == 1 and not ok:
                    fall_sound.play()
                    text = 'Кто здесь?'
                    pygame.mouse.set_visible(True)
                    ok = True
                    pygame.time.delay(100)
                elif ok and click[0] == 1:
                    self.hall3(True)
                    win = False
            else:
                pygame.mouse.set_visible(True)

            pygame.display.update()

    def computer(self, win):
        pygame.mouse.set_visible(True)
        while win:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    win = False
            game.blit(pygame.image.load("level_3/компьютер.png"), (0, 0))
            win = button_exit.draw(750, 800, 800, 850)
            print_text('Очень странно...', 100, 650)
            print_text('По базе все номера заняты. Кто же их забронировал?', 300, 700)
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            if 450 < mouse[0] < 1200 and 100 < mouse[1] < 600:
                game.blit(pygame.image.load("level_1/курсор.png"), mouse)
                pygame.mouse.set_visible(False)
                if click[0] == 1:
                    pygame.mouse.set_visible(True)
                    self.computer2(True)
                    win = False
            else:
                pygame.mouse.set_visible(True)

            pygame.display.update()

    def hall2(self, win):
        while win:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    win = False
            game.blit(pygame.image.load("level_3/холл1.png"), (0, 0))
            win = button_exit.draw(750, 800, 800, 850)
            print_text('                             Если и правда тут никого нет, то почему горит свет?', 100, 650)
            print_text('                                             А что если посмотреть в компьютере!', 300, 700)
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            if 200 < mouse[0] < 350 and 550 < mouse[1] < 700:
                game.blit(pygame.image.load("level_1/курсор.png"), mouse)
                pygame.mouse.set_visible(False)
                if click[0] == 1:
                    self.computer(True)
                    win = False
            else:
                pygame.mouse.set_visible(True)

            pygame.display.update()

    def number(self, win):
        game.blit(pygame.image.load("level_3/номерр.jpg"), (0, 0))
        while win:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    win = False
            win = button_exit.draw(750, 800, 800, 850)
            print_text('И тут пусто', 300, 700)
            a = button_choise.draw(300, 750, "В коридор", 60, 'ok')
            if a:
                self.hall2(True)
                win = False

    def number_gg(self, win):
        game.blit(pygame.image.load("level_3/номер.jpg"), (0, 0))
        while win:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    win = False
            win = button_exit.draw(750, 800, 800, 850)
            print_text('После всего, чего мне довелось пережить,', 100, 650)
            print_text('эта комната просто шикарна', 300, 700)
            a = button_choise.draw(1000, 750, "В другие комнаты", 25, 'kitchen')
            if a:
                self.number(True)
                win = False

    def hall(self, win):
        while win:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    win = False
            game.blit(pygame.image.load("level_3/холл1.png"), (0, 0))
            win = button_exit.draw(750, 800, 800, 850)
            print_text('                               Ауууу! Тут кто-нибудь есть? Мне нужен номер', 100, 650)
            print_text('                                                  Кажется, никого', 300, 700)
            a = button_choise.draw(300, 750, "Найти комнату", 30, 'hallway')
            if a:
                self.number_gg(True)
                win = False
            pygame.display.update()

        game.blit(pygame.image.load("меню,кнопки/меню.jpg"), (0, -80))
        pygame.display.update()
