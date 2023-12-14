import pygame
from game_child import Player
pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()

game = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
but_sound = pygame.mixer.Sound("меню,кнопки/кнопка.wav")


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


class Hotel():
    def end(self, win):
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

    def game_child(self, win):
        game.blit(pygame.image.load("level_3/bg_gamechild.png"), (0, 0))
        game.blit(pygame.image.load("level_3/bg2_gamechild.png"), (0, 100))
        FPS = 30
        clock = pygame.time.Clock()
        pygame.display.update()
        all_sprites_list = pygame.sprite.Group()

        player = Player(100, 690)
        all_sprites_list.add(player)

        while win:
            game.blit(pygame.image.load("level_3/bg_gamechild.png"), (0, 0))
            game.blit(pygame.image.load("level_3/bg2_gamechild.png"), (0, 100))
            win = button_exit.draw(750, 800, 800, 850)
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

            if player.alive:
                all_sprites_list.update()
                all_sprites_list.draw(game)
            else:
                player.alive = True
                player.rect.x = 130
                player.rect.y = 690

            pygame.display.flip()
            clock.tick(FPS)

    def computer(self, win):
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

    def door(self, win):
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

    def game_sleep(self):
        pass

    def number(self, win):
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

    def number_gg(self, win):
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

    def hall(self, win):
        game.blit(pygame.image.load("level_3/холл1.png"), (0, 0))
        pygame.display.update()
        while win:
            for event in pygame.event.get():
                win = button_exit.draw(750, 800, 800, 850)
                if event.type == pygame.QUIT:
                    win = False
                a = button_choise.draw(self, 300, 750, "  Войти", 60, 'hallway')
                if a:
                    self.game_child(True)
                    win = False
        game.blit(pygame.image.load("меню,кнопки/меню.jpg"), (0, -80))
        pygame.display.update()