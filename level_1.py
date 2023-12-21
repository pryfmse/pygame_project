import pygame
from game_lab import Player
from game_lab import Enemy
from game_lab import Wall
pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()


game = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
but_sound = pygame.mixer.Sound("меню,кнопки/кнопка.wav")


def print_text(message, x, y, font_size=30, font_color=(255, 255, 255), font_type="меню,кнопки/a ConceptoTitulRough.ttf"):
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(message, True, font_color)
    game.blit(text, (x, y))


class Button:
    def __init__(self, inactive, active, mess=None):
        self.inactive = inactive
        self.active = active
        self.mess = mess

    def draw(self, x, y, x_mes, y_mes):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if self.mess == 'exit':
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
        else:
            if x + 10 < mouse[0] < x + 100 and y < mouse[1] < y + 100:
                game.blit(self.active, (x, y))
                pygame.display.update()
                if click[0] == 1:
                    but_sound.play()
                    while not (click[0] == 1 and 0 < mouse[0] < 700 and 0 < mouse[1] < 900):
                        game.blit(pygame.image.load("level_1/game_lab/кнопка_прямоугольник.png"), (800, 100))
                        print_text("Ваша задача - клавишами 'вверх', 'вниз',", 880, 150)
                        print_text("'влево', 'вправо' вывести героя из", 880, 200)
                        print_text(" здания, не наткнувшись ни на кого", 880, 250)
                        pygame.display.update()
            else:
                game.blit(self.inactive, (x, y))
                pygame.display.update()


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


button_exit = Button(pygame.image.load("меню,кнопки/кнопка_овал.png"),
                     pygame.image.load("меню,кнопки/кнопкаlight_овал.png"), 'exit')
button_choise = Picture_button()


class Hostel():
    def game_lab(self, win=True):
        game.blit(pygame.image.load("level_1/лабиринт.jpg"), (0, 0))
        game.fill((0, 0, 0))
        FPS = 60
        clock = pygame.time.Clock()
        pygame.display.update()
        all_sprites_list = pygame.sprite.Group()
        wall_list = pygame.sprite.Group()
        wall_coords = [
            [100, 100, 20, 700],
            [1480, 100, 20, 580],
            [400, 100, 20, 300],
            [400, 600, 20, 200],
            [800, 400, 20, 200],
            [1200, 230, 20, 550],
            [1050, 230, 20, 130],
            [100, 100, 1380, 20],  # gor
            [100, 780, 1380, 20],
            [100, 600, 130, 20],
            [330, 600, 160, 20],
            [400, 400, 420, 20],
            [1300, 500, 200, 20],
            [1050, 350, 300, 20],
            [800, 600, 250, 20],
            [600, 230, 450, 20]
        ]
        for coord in wall_coords:
            wall = Wall(coord[0], coord[1], coord[2], coord[3])
            wall_list.add(wall)
            all_sprites_list.add(wall)

        enemies_list = pygame.sprite.Group()
        enemies_coord = [[120, 620, 200, 3, 'gor', 'level_1/game_lab/enemies1_вниз.png', 'level_1/game_lab/enemies1_вверх.png',
                          'level_1/game_lab/enemies1_влево.png', 'level_1/game_lab/enemies1_вправо.png'],
                         [500, 150, 850, 6, 'gor', 'level_1/game_lab/enemies2_вниз.png', 'level_1/game_lab/enemies2_вверх.png',
                          'level_1/game_lab/enemies2_влево.png', 'level_1/game_lab/enemies2_вправо.png'],
                         [1250, 520, 150, 6, 'gor', 'level_1/game_lab/enemies3_вниз.png', 'level_1/game_lab/enemies3_вверх.png',
                          'level_1/game_lab/enemies3_влево.png', 'level_1/game_lab/enemies3_вправо.png'],
                         [850, 400, 300, 6, 'gor', 'level_1/game_lab/enemies4_вниз.png', 'level_1/game_lab/enemies4_вверх.png',
                          'level_1/game_lab/enemies4_влево.png', 'level_1/game_lab/enemies4_вправо.png'],
                         [420, 700, 700, 6, 'gor', 'level_1/game_lab/enemies5_вниз.png', 'level_1/game_lab/enemies5_вверх.png',
                          'level_1/game_lab/enemies5_влево.png', 'level_1/game_lab/enemies5_вправо.png'],
                         [250, 250, 400, 6, 'vert', 'level_1/game_lab/enemies6_вниз.png', 'level_1/game_lab/enemies6_вверх.png',
                          'level_1/game_lab/enemies6_влево.png', 'level_1/game_lab/enemies6_вправо.png'],
                         [1100, 400, 300, 3, 'vert', 'level_1/game_lab/enemies7_вниз.png', 'level_1/game_lab/enemies7_вверх.png',
                          'level_1/game_lab/enemies7_влево.png', 'level_1/game_lab/enemies7_вправо.png'],
                         [1400, 600, 100, 3, 'vert', 'level_1/game_lab/enemies8_вниз.png', 'level_1/game_lab/enemies8_вверх.png',
                          'level_1/game_lab/enemies8_влево.png', 'level_1/game_lab/enemies8_вправо.png']]
        for coord in enemies_coord:
            enemy = Enemy(coord[0], coord[1], coord[2], coord[3], coord[4], coord[5], coord[6], coord[7], coord[8])
            enemies_list.add(enemy)
            all_sprites_list.add(enemy)

        player = Player(100, 690)
        player.walls = wall_list
        all_sprites_list.add(player)
        player.enemies = enemies_list

        while win:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    win = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        player.change_x = -5
                    if event.key == pygame.K_RIGHT:
                        player.change_x = 5
                    if event.key == pygame.K_UP:
                        player.change_y = -5
                    if event.key == pygame.K_DOWN:
                        player.change_y = 5
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        player.change_x = 0
                    if event.key == pygame.K_RIGHT:
                        player.change_x = 0
                    if event.key == pygame.K_UP:
                        player.change_y = 0
                    if event.key == pygame.K_DOWN:
                        player.change_y = 0

            game.blit(pygame.image.load("level_1/лабиринт.jpg"), (0, 0))
            win = button_exit.draw(750, 800, 800, 850)

            if player.alive:
                all_sprites_list.update()
                all_sprites_list.draw(game)
            else:
                player.alive = True
                player.rect.x = 130
                player.rect.y = 690

            pygame.display.flip()

    def basement(self, win):
        game.blit(pygame.image.load("level_1/подвал.jpg"), (0, 0))
        pygame.display.update()
        while win:
            for event in pygame.event.get():
                win = button_exit.draw(750, 800, 800, 850)
                if event.type == pygame.QUIT:
                    win = False
                print_text('Привет. Ты первокурсник?', 100, 650)
                print_text('Меня Коля зовут, будем знакомы. Провести тебе экскурсию?', 300, 700)
                pygame.display.update()
                a = button_choise.draw(1000, 750, "Давай", 60, 'kitchen')
                if a:
                    self.kitchen_our(True)
                    win = False

    def room2(self, win):
        game.blit(pygame.image.load("level_1/комната.png"), (0, 0))
        game.blit(pygame.image.load("level_1/сосед.png"), (0, 180))
        pygame.display.update()
        while win:
            for event in pygame.event.get():
                win = button_exit.draw(750, 800, 800, 850)
                if event.type == pygame.QUIT:
                    win = False
                print_text('Привет. Ты первокурсник? Меня Коля зовут, ', 600, 650)
                print_text('будем знакомы. Провести тебе экскурсию?', 650, 700)
                pygame.display.update()
                a = button_choise.draw(1100, 730, "Давай", 60, 'kitchen')
                if a:
                    self.kitchen_our(True)
                    win = False

    def to_basement(self, win):
        game.blit(pygame.image.load("level_1/у подвала.png"), (0, 0))
        game.blit(pygame.image.load("level_1/сосед.png"), (0, 180))
        pygame.display.update()
        while win:
            for event in pygame.event.get():
                win = button_exit.draw(750, 800, 800, 850)
                if event.type == pygame.QUIT:
                    win = False
                print_text('Видишь у окна спуск в подвал?', 600, 650)
                print_text('Лучше тебе туда не соваться', 650, 700)
                pygame.display.update()
                a = button_choise.draw(1000, 750, "Почему?", 60, 'kitchen')
                if a:
                    self.game_lab(True)
                    win = False
                    # for i in ["level_1/с1.png", "level_1/с2.png", "level_1/с3.png"]:
                    #     game.blit(pygame.image.load("level_1/у подвала.png"), (0, 0))
                    #     game.blit(pygame.image.load(i), (0, 180))
                    #     print_text('Не задавай лишних вопросов', 800, 700)
                    #     pygame.display.update()
                    #     pygame.time.delay(100)
                    # pygame.time.delay(400)
                    # b = button_choise.draw(1000, 750, "Не буду", 60, 'kitchen')
                    # if b:
                    #     print_text('Вот и славно. Пойдем назад', 800, 700)
                    #     pygame.display.update()
                    #     c = button_choise.draw(1000, 750, "Пойдем", 60, 'kitchen')
                    #     if c:
                    #         self.room2(True)
                    #         win = False


    def kitchen_our(self, win):
        game.blit(pygame.image.load("level_1/кухня.jpg"), (0, 0))
        game.blit(pygame.image.load("level_1/сосед.png"), (0, 180))
        while win:
            for event in pygame.event.get():
                win = button_exit.draw(750, 800, 800, 850)
                if event.type == pygame.QUIT:
                    win = False
                print_text('Всё просто: приготовил - съел. Чужое не брать,', 600, 650)
                print_text('а то могут быть проблемы', 650, 700)
                pygame.display.update()
                a = button_choise.draw(1000, 750, "  Понял", 60, 'дальше')
                if a:
                    self.to_basement(True)
                    win = False

    def room(self, win):
        game.blit(pygame.image.load("level_1/комната.png"), (0, 0))
        game.blit(pygame.image.load("level_1/сосед.png"), (0, 180))
        pygame.display.update()
        while win:
            for event in pygame.event.get():
                win = button_exit.draw(750, 800, 800, 850)
                if event.type == pygame.QUIT:
                    win = False
                print_text('Привет. Ты первокурсник? Меня Коля зовут, ', 600, 650)
                print_text('будем знакомы. Провести тебе экскурсию?', 650, 700)
                pygame.display.update()
                a = button_choise.draw(1000, 750, "  Давай", 60, 'kitchen')
                if a:
                    self.kitchen_our(True)
                    win = False

    def hallway(self, win):
        game.blit(pygame.image.load("level_1/коридор.png"), (0, 0))
        pygame.display.update()
        while win:
            for event in pygame.event.get():
                win = button_exit.draw(750, 800, 800, 850)
                if event.type == pygame.QUIT:
                    win = False
                print_text('Как же понять, куда идти?', 100, 700)
                pygame.display.update()
                a = button_choise.draw(1000, 750, "В свою комнату", 30, 'room')
                if a:
                    self.room(True)
                    win = False

    def entry(self, win):
        game.blit(pygame.image.load("level_1/начало.png"), (0, 0))
        pygame.display.update()
        while win:
            for event in pygame.event.get():
                win = button_exit.draw(750, 800, 800, 850)
                if event.type == pygame.QUIT:
                    win = False
                print_text('Ну и местечко...', 300, 700)
                pygame.display.update()
                a = button_choise.draw(300, 750, "Подняться", 50, 'hallway')
                if a:
                    self.game_lab(True)
                    win = False
        game.blit(pygame.image.load("меню,кнопки/меню.jpg"), (0, -80))
        pygame.display.update()