import os
import random

import pygame.image

pygame.mixer.pre_init(44100, -16, 1, 512)

pygame.init()

game = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
but_sound = pygame.mixer.Sound("меню,кнопки/кнопка.wav")
start_sound = pygame.mixer.Sound("level_2/вход.wav")
hallway_sound = pygame.mixer.Sound("level_2/коридор.wav")
kitchen_sound = pygame.mixer.Sound("level_2/кухня.wav")
door_sound_yes = pygame.mixer.Sound("level_2/ага.wav")
door_sound_no = pygame.mixer.Sound("level_2/не-а.wav")
fly_sound = pygame.mixer.Sound("level_2/мухи.wav")


# печать текста на экране
def print_text(message, x, y, font_size=30, font_color=(255, 255, 255),
               font_type="меню,кнопки/a ConceptoTitulRough.ttf"):
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(message, True, font_color)
    game.blit(text, (x, y))


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


class Player(pygame.sprite.Sprite):  # класс игрока в мини-игре "побег"
    def __init__(self):
        super().__init__(player_group, all_sprites)
        self.img = ['level_2/game_road/player_1.png', 'level_2/game_road/player_3.png']
        self.a = 0
        self.image = pygame.image.load('level_2/game_road/player_2.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = 500
        self.rect.y = 675
        self.alive = True

    def update(self):
        if pygame.sprite.spritecollideany(self, enemy_sprites):
            self.alive = False


class Picture_button():  # класс кнопки с изображением
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


class Camera:  # класс камеры в мини-игре "лабиринт"
    # зададим начальный сдвиг камеры
    def __init__(self):
        self.dy = 0

    # сдвинуть объект obj на смещение камеры
    def apply(self, obj):
        obj.rect.y += self.dy

    # позиционировать камеру на объекте target
    def update(self, target):
        self.dy = -(target.rect.y + target.rect.h // 2 - 1500 // 2)


class Tile(pygame.sprite.Sprite):  # класс блоков в мини-игре "побег"
    def __init__(self, tile_type, pos_x, pos_y):
        if tile_type != 'barrier' and tile_type != 'water':
            super().__init__(tiles_group, all_sprites)
        else:
            super().__init__(enemy_sprites, all_sprites)
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(
            240 * pos_x, 150 * pos_y)


class Enemy(pygame.sprite.Sprite):  # класс врагов в мини-игре "побег"
    def __init__(self, type_e, pos_x, pos_y, t, speed):
        super().__init__(enemy_sprites, all_sprites)
        self.coll = []
        if type_e == 'spider':
            self.coll = type_e
            self.a = 0
            self.image = en_image[type_e][0]
        else:
            self.image = en_image[type_e]
        self.rect = self.image.get_rect().move(
            pos_x, pos_y)
        self.speed = speed
        self.t = t

    def update(self):
        if self.t == 'r':
            if self.rect.x <= 1450:
                self.rect.x += self.speed
            else:
                self.rect.x = -30
        elif self.t == 'l':
            if self.rect.x >= 0:
                self.rect.x -= self.speed
            else:
                self.rect.x = 1500
        else:
            self.image = en_image[self.coll][(self.a + 1) % 4]
            self.a += 1
            if self.rect.x <= 1450:
                self.rect.x += self.speed
            else:
                self.rect.x = -30


class Results(pygame.sprite.Sprite):  # класс выведения результатов в мини-игре "побег"
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


def load_image(name, color_key=None):  # чтение карты уровня из файла txt
    fullname = os.path.join('level_2', name)
    try:
        image = pygame.image.load(fullname).convert_alpha()
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)

    if color_key is not None:
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    else:
        image = image.convert_alpha()
    return image


def load_level(filename):  # чтение уровня
    filename = "level_2/" + filename
    # читаем уровень, убирая символы перевода строки
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]

    # и подсчитываем максимальную длину
    max_width = max(map(len, level_map))

    # дополняем каждую строку пустыми клетками ('.')
    return list(map(lambda x: x.ljust(max_width, '.'), level_map))


def generate_level(level):  # генерация уровня
    for y in range(len(level) - 1, -1, -1):
        for x in range(len(level[y]) - 1, -1, -1):
            if level[y][x] == '"':
                Tile('grass', x, y - 17)
            elif level[y][x] == '-':
                Tile('water', x, y - 17)
            elif level[y][x] == '_':
                Tile('raft', x, y - 17)
            elif level[y][x] == '^':
                Tile('road', x, y - 17)
                if x == 0:
                    choices = ['red_car_left', 'red_car_right', 'blue_car_left', 'biue_car_right']
                    a = random.choice(choices)
                    n1 = random.randint(0, 1500)
                    n2 = n1 + random.randint(200, 700)
                    if a == 'red_car_right' or a == 'biue_car_right':
                        Enemy(a, n1, (y - 17) * 150 + 5, 'r', 15)
                        Enemy(a, n2, (y - 17) * 150 + 5, 'r', 15)
                    else:
                        Enemy(a, n1, (y - 17) * 150 + 5, 'l', 15)
                        Enemy(a, n2, (y - 17) * 150 + 5, 'l', 15)
            elif level[y][x] == "'":
                Tile('barrier', x, y - 17)
    Enemy('spider', random.randint(0, 1500), -445, '', 20)
    Enemy('spider', random.randint(0, 1500), -1795, '', 20)
    Enemy('spider', random.randint(0, 1500), -2380, '', 20)


button_exit = Button()
button_choise = Picture_button()
button_replace = Picture_button('level_2/game_sheep/кнопка_заново_светлая.png',
                                'level_2/game_sheep/кнопка_заново_темная.png', 150)
all_sprites = pygame.sprite.Group()
player_group = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
enemy_sprites = pygame.sprite.Group()
tile_images = {
    'grass': load_image('game_road/трава.png'),
    'water': load_image('game_road/вода.png'),
    'road': load_image('game_road/road.png'),
    'barrier': load_image('game_road/трава_преграда.png'),
    'raft': load_image('game_road/плот.png')
}
en_image = {
    'red_car_left': load_image('game_road/красная_машина_влево.png'),
    'red_car_right': load_image('game_road/красная_машина_вправо.png'),
    'blue_car_left': load_image('game_road/синяя_машина_влево.png'),
    'biue_car_right': load_image('game_road/синяя_машина_вправо.png'),
    'spider': [load_image('game_road/паук_1.png'), load_image('game_road/паук_2.png'),
               load_image('game_road/паук_3.png'), load_image('game_road/паук_4.png')]
}


class Communalka():  # главный класс второго уровня
    def game_sheep(self, win):  # мини-игра "овечки"
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
                                field[x][y - 1] = '01' if field[x][y - 1] == '2' else '51'
                                field[x][y - 2] = '2' if field[x][y - 2] == '0' else '52'
                                field[x][y] = field[x][y][:-1]
                                x, y = x, y - 1
                    if event.key == pygame.K_RIGHT:
                        if not ((x == 0 and y == 3) or (x == 3 and y == 3) or y == 4):
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
                                field[x][y + 1] = '01' if field[x][y + 1] == '2' else '51'
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
                                field[x - 1][y] = '01' if field[x - 1][y] == '2' else '51'
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
                                field[x + 1][y] = '01' if field[x + 1][y] == '2' else '51'
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
                        if not (j == 0 and i == 4) and not (j == 3 and i == 4):
                            game.blit(pygame.image.load("level_2/game_sheep/клетка.png"),
                                      (450 + 130 * i, 200 + 130 * j))
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

    def game_road(self, win):  # мини-игра "побег"
        generate_level(load_level('game_road/карта.txt'))
        fly_sound.stop()
        player = Player()
        camera = Camera()
        end = False
        start = pygame.time.get_ticks()
        now = []
        sprite = pygame.sprite.Group()
        res = Results()
        sprite.add(res)
        a = 2.0
        d = 0
        while win:
            for event in pygame.event.get():
                if not end:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                            if player.rect.x > 0:
                                player.rect.x += -125
                                player.image = pygame.image.load(player.img[player.a % 2]).convert_alpha()
                                player.a += 1
                        if event.key == pygame.K_RIGHT:
                            if player.rect.x < 1450:
                                player.rect.x += 125
                                player.image = pygame.image.load(player.img[player.a % 2]).convert_alpha()
                                player.a += 1
                        if event.key == pygame.K_UP:
                            if player.rect.y > 0:
                                player.rect.y += -75
                                a += 0.5
                                d += 1
                                player.image = pygame.image.load(player.img[player.a % 2]).convert_alpha()
                                player.a += 1
                        if event.key == pygame.K_DOWN:
                            if player.rect.y < 750:
                                player.rect.y += 75
                                a -= 0.5
                                d += -1
                                player.image = pygame.image.load(player.img[player.a % 2]).convert_alpha()
                                player.a += 1

            # изменяем ракурс камеры
            camera.update(player)
            # обновляем положение всех спрайтов
            if 19 > a > 2:
                for sprite in all_sprites:
                    camera.apply(sprite)
            all_sprites.update()
            all_sprites.draw(game)
            print_text('Двигайтесь вперед, чтобы убежать.', 1000, 20)
            print_text('Не угодите в беду!', 1000, 60)
            win = button_exit.draw(750, 800, 800, 850)

            if not player.alive:
                for _ in range(d):
                    player.rect.y += 75
                    camera.update(player)
                    for sprite in all_sprites:
                        camera.apply(sprite)
                    all_sprites.update()
                d = 0
                a = 2.0
                all_sprites.draw(game)
                player.alive = True

            if player.rect.y < 0 and not end:
                now = pygame.time.get_ticks()
                end = True
                all_sprites.add(res)

            if res.rect.x == 400:
                print_text('Вы выиграли!', 500, 300, 60)
                print_text(f'Время игры: {str((now - start) / 1000)} сек', 500, 400)
            pygame.display.flip()

    def room(self, win):  # комната Геннадия
        game.blit(pygame.image.load("level_2/комната_Геннадия_1.jpg.png"), (0, 0))
        fly_sound.play()
        while win:
            for event in pygame.event.get():
                win = button_exit.draw(750, 800, 800, 850)
                if event.type == pygame.QUIT:
                    win = False
                print_text('О Боже! Кто эти люди?', 300, 700)
                pygame.display.update()
                a = button_choise.draw(1000, 750, "Бежать!", 30, True)
                if a:
                    self.game_road(win)
                    win = False

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
                a = button_choise.draw(1000, 750, "Разложить вещи", 30, True)
                if a:
                    while win:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pass
                        game.blit(pygame.image.load("level_2/комнатаГГ_вещи.png"), (-100, 0))
                        print_text('"День был очень утомительным"', 300, 700)
                        win = button_exit.draw(750, 800, 800, 850)
                        c = button_choise.draw(300, 750, "Лечь спать", 30, True)
                        pygame.display.flip()
                        if c:
                            self.game_sheep(True)
                            win = False

    def behind_door(self, win):  # у двери
        game.blit(pygame.image.load("level_2/у двери.jpg"), (0, 0))
        now = True
        while win:
            for event in pygame.event.get():
                win = button_exit.draw(750, 800, 800, 850)
                mouse = pygame.mouse.get_pos()
                click = pygame.mouse.get_pressed()
                if event.type == pygame.QUIT:
                    win = False
                if 750 < mouse[0] < 950 and 50 < mouse[1] < 850:
                    if not now:
                        door_sound_yes.play()
                        pygame.time.delay(300)
                        now = True
                    if click[0] == 1:
                        self.room(win)
                        win = False
                else:
                    if now:
                        door_sound_no.play()
                        pygame.time.delay(300)
                        now = False
                pygame.display.update()

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
                a = button_choise.draw(1000, 750, "За чайником", 30, True)
                if a:
                    self.behind_door(win)
                    win = False
                b = button_choise.draw(300, 750, "Где моя комната?", 30, True)
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
                a = button_choise.draw(1000, 750, "Пить чай", 60, True)
                if a:
                    self.kitchen(True)
                    win = False
                b = button_choise.draw(300, 750, "Сначала моя комната", 25, True)
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
                a = button_choise.draw(300, 750, "  Войти", 60, True)
                if a:
                    self.hallway(True)
                    win = False
        game.blit(pygame.image.load("меню,кнопки/меню.jpg"), (0, -80))
        pygame.display.update()
