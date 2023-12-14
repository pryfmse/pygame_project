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
        # # проверка, не врезается ли в стену
        # block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        # for block in block_hit_list:
        #     if self.change_x > 0:
        #         self.rect.right = block.rect.left
        #     else:
        #         self.rect.left = block.rect.right

        self.rect.y += self.change_y
        # # проверка, не врезается ли в стену
        # block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        # for block in block_hit_list:
        #     if self.change_y > 0:
        #         self.rect.bottom = block.rect.top
        #     else:
        #         self.rect.top = block.rect.bottom


# class Wall(pygame.sprite.Sprite):
#     def __init__(self, x, y, width, height):
#         super().__init__()
#
#         self.image = pygame.Surface([width, height])
#         self.image.fill((229, 228, 226))
#
#         self.rect = self.image.get_rect()
#         self.rect.x = x
#         self.rect.y = y


pygame.init()
