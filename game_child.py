import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, wall=pygame.sprite.Group(), grass=pygame.sprite.Group(), barrier=pygame.sprite.Group()):
        super().__init__()

        self.image = pygame.image.load('level_3/game_child/ГГ_стоит.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.change_x = 0
        self.change_y = 0
        self.walls = None
        self.up = 0
        self.start = pygame.time.get_ticks()
        self.img_right = ['level_3/game_child/ГГ_вправо1.png', 'level_3/game_child/ГГ_вправо2.png',
                          'level_3/game_child/ГГ_вправо3.png']
        self.right = 0
        self.img_left = ['level_3/game_child/ГГ_влево1.png', 'level_3/game_child/ГГ_влево2.png',
                         'level_3/game_child/ГГ_влево3.png']
        self.left = 0

        self.barrier = barrier
        self.walls = wall
        self.grass = grass
        self.alive = True

    def update(self):
        if self.change_x == 0:
            self.image = pygame.image.load('level_3/game_child/ГГ_стоит.png').convert_alpha()
        elif self.change_x > 0:
            self.image = pygame.image.load(self.img_right[self.right % 3]).convert_alpha()
            self.right += 1
        elif self.change_x < 0:
            self.image = pygame.image.load(self.img_left[self.left % 3]).convert_alpha()
            self.left += 1

        if self.change_y != 0 and self.start > 2000:
            self.rect.y -= 100
            self.up += 1
            self.start = pygame.time.get_ticks()

        elif self.up > 0 and self.start > 1000:
            self.up -= 1
            self.rect.y += 100
            self.start = pygame.time.get_ticks()

        self.rect.x += self.change_x

        # в верхней точке земли
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
            self.rect.y = block.rect.top


class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, img):
        super().__init__()
        self.image = pygame.image.load(img).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Camera:
    # зададим начальный сдвиг камеры
    def __init__(self):
        self.dx = 0

    # сдвинуть объект obj на смещение камеры
    def apply(self, obj):
        obj.rect.x += self.dx

    # позиционировать камеру на объекте target
    def update(self, target):
        self.dx = -(target.rect.x + target.rect.w // 2 - 900 // 2)


class Fire(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()


pygame.init()
