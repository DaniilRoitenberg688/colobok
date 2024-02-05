import pygame

# группа игрока
player_group = pygame.sprite.Group()

# группа бочек
barrels_group = pygame.sprite.Group()

# группа всех спрайтов
all_sprites_group = pygame.sprite.Group()

# группа стен
walls_group = pygame.sprite.Group()

# группа патронов
patrons_group = pygame.sprite.Group()

# группа врагов
enemies_group = pygame.sprite.Group()

# группа частиц
particles_group = pygame.sprite.Group()

# группа пакмена
pacman_group = pygame.sprite.Group()

# группа победного места
win_place_group = pygame.sprite.Group()

# список всех групп
all_groups = [player_group, barrels_group, all_sprites_group, walls_group, patrons_group, enemies_group,
              particles_group, pacman_group, win_place_group]
