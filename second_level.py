import time

from constants import *
from functions import load_level, clear_groups, pause_menu, win_window, draw_pacman_hp, load_image
from game_objects import generate_level, die_of_hero
from groups import *


def second_level():
    # создаем экран
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    # загружаем карту
    map = load_level('map2.txt')

    # определяем игрока и пакмена
    player, pacman = generate_level(map)

    # живой или нет
    alive = True

    # идет ли анимация смерти
    die_animation_is_running = False

    # часы
    clock = pygame.time.Clock()

    # время длительности анимации
    animation_time = 0

    running = True

    # позиционирование объектов
    for object in all_sprites_group:
        object.rect.x -= 50
        object.rect.y += 150
    player.rect.x -= 50
    player.rect.y += 150

    # есть ли пауза
    is_pause = False

    # победил или нет
    win_or_not = False

    # анимация смерти пакмена
    pacman_die_animation = False

    # начальное время
    start_time = time.time()
    finish_time = 0

    while running:
        screen.fill(BACKGROUND_GREY)

        # пробегаемся по событиям
        for event in pygame.event.get():
            # если закрыто окно чистим группы и завершаем цикл
            if event.type == pygame.QUIT:
                clear_groups()
                running = False

            # если не умер и е пауза обновляем игрока
            if alive and not is_pause and not win_or_not:
                player_group.update(event, map, True)

            if event.type == pygame.KEYDOWN:
                # если ESCAPE запускаем паузу
                if event.key == pygame.K_ESCAPE:
                    is_pause = True

            # если победа, то ждем нажатия клавиши
            if win_or_not:
                if event.type == pygame.KEYDOWN:
                    running = False

            # если пауза отслеживаем нажатие игрока
            if is_pause:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # получаем координаты клика
                    x = event.pos[0]
                    y = event.pos[1]

                    if 100 < x < 500 and 100 < y < 500:
                        # если нажата кнопка продолжить убираем паузу
                        if 130 < x < 280 and 295 < y < 445:
                            is_pause = False
                            continue

                        # если нажата кнопка выход выходим
                        if 325 < x < 625 and 295 < y < 445:
                            running = False
                            clear_groups()

        # если пакмен умер, то запускаем звук смерти и запускаем анимацию смерти пакмена и фиксируем время окончания
        if pacman.hp == 0 and not pacman_die_animation and not win_or_not:
            pygame.mixer.music.load('data/sounds/pacman_die.mp3')
            pygame.mixer.music.set_volume(0.5)
            pygame.mixer.music.play(0)
            die_of_hero(pacman.rect.x, pacman.rect.y, 0)
            pacman.kill()
            pacman_die_animation = True
            finish_time = time.time()

        # если касаемся врага умираем
        if pygame.sprite.spritecollideany(player, enemies_group):
            alive = False

        # если умер запускаем анимацию смерти и звук
        if not alive and not die_animation_is_running:
            pygame.mixer.music.load('data/sounds/player_die.mp3')
            pygame.mixer.music.set_volume(0.5)
            pygame.mixer.music.play(0)
            die_animation_is_running = True
            die_of_hero(player.rect.x, player.rect.y, 1)
            player.kill()

        # если игра идет обновляем остальных спрайтов
        if alive and not is_pause and not win_or_not and not pacman_die_animation:
            all_sprites_group.update()
            enemies_group.update()
            all_sprites_group.draw(screen)
            player_group.draw(screen)
            enemies_group.draw(screen)
            draw_pacman_hp(screen, pacman.hp)

        # если анимация смерти игрока ждем какое-то время и выходим
        if die_animation_is_running:
            if animation_time == 40:
                clear_groups()
                running = False
            particles_group.update()
            all_sprites_group.draw(screen)
            player_group.draw(screen)
            enemies_group.draw(screen)
            particles_group.draw(screen)
            draw_pacman_hp(screen, pacman.hp)
            animation_time += 1

        # если идет анимация смерти пакмена ждем какое-то время и запускаем окно победы и звук
        if pacman_die_animation and not win_or_not:
            if animation_time == 80:
                clear_groups()
                pygame.mixer.music.load('data/sounds/si.mp3')
                pygame.mixer.music.set_volume(0.5)
                pygame.mixer.music.play(1)
                win_or_not = True
                pacman_die_animation = False
            particles_group.update()
            all_sprites_group.draw(screen)
            player_group.draw(screen)
            enemies_group.draw(screen)
            particles_group.draw(screen)
            draw_pacman_hp(screen, pacman.hp)
            animation_time += 1

        # если пауза рисуем окно паузы
        if is_pause:
            pause_menu(screen, 100, 100)

        # если победа рисуем победное окно
        if win_or_not:
            clear_groups()
            win_window(screen, 100, 100, finish_time - start_time - 20)

        pygame.display.set_caption('Уровень 2')
        pygame.display.set_icon(load_image('full_red.png'))

        clock.tick(FPS)
        pygame.display.flip()


if __name__ == '__main__':
    second_level()
