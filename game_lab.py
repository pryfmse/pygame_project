import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, img='level_1/game_lab/player_стоитпередом.png'):
        super().__init__()

        self.image = pygame.image.load(img).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.change_x = 0
        self.change_y = 0
        self.walls = None

        self.enemies = pygame.sprite.Group()
        self.alive = True

    def update(self):
        # движение вправо - влево
        self.rect.x += self.change_x
        # проверка, не врезается ли в стену
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:
                self.rect.left = block.rect.right

        self.rect.y += self.change_y
        # проверка, не врезается ли в стену
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom

        if pygame.sprite.spritecollideany(self, self.enemies):
            self.alive = False


class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill((229, 228, 226))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, walk, a, orien, img_down, img_up, img_left, img_right):
        super().__init__()

        self.img_down = img_down
        self.img_up = img_up
        self.img_left = img_left
        self.img_right = img_right
        self.x = x
        self.y = y
        self.speed = a
        self.orien = orien

        if orien == 'gor':
            self.image = pygame.image.load(self.img_right).convert_alpha()
            self.start = x
            self.stop = x + walk
            self.direction = 1
        else:
            self.image = pygame.image.load(self.img_down).convert_alpha()
            self.start = y
            self.stop = y + walk
            self.direction = 1
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        if self.orien == 'gor':
            if self.rect.x > self.stop:
                self.image = pygame.image.load(self.img_left).convert_alpha()
                self.direction = -1
            elif self.rect.x < self.start:
                self.image = pygame.image.load(self.img_right).convert_alpha()
                self.direction = 1
            self.rect.x += self.direction * self.speed
        else:
            if self.rect.y > self.stop:
                self.image = pygame.image.load(self.img_up).convert_alpha()
                self.direction = -1
            elif self.rect.y < self.start:
                self.image = pygame.image.load(self.img_down).convert_alpha()
                self.direction = 1
            self.rect.y += self.direction * self.speed


pygame.init()
