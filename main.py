import pygame

from constants import WIDTH, HEIGHT, GREY
from functions import load_image, main_exit
from level_menu import level_menu


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    running = True

    # загрузка наипрекрасниейшего фона
    image = load_image('fon.png')

    # загрузка текста с названием игры
    font_for_name = pygame.font.Font('data/font/minecraft-ten-font-cyrillic.ttf', 43)
    name_of_game = font_for_name.render('COLOBOK ADVENTURE', True, (179, 40, 33))

    # загрузка текста с отображением инструкций
    font_for_space = pygame.font.Font('data/font/minecraft-ten-font-cyrillic.ttf', 35)
    font_for_escape = pygame.font.Font('data/font/minecraft-ten-font-cyrillic.ttf', 20)
    first_text = font_for_space.render('Press SPACE to start', True, GREY)
    second_text = font_for_escape.render('ESCAPE to exit', True, (188, 188, 188))

    # отрисовка всех элементов
    screen.fill((255, 255, 255))
    screen.blit(image, (20, 60))
    screen.blit(name_of_game, (25, 30))
    screen.blit(first_text, (55, 580))
    screen.blit(second_text, (200, 630))

    pygame.display.flip()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                # если нажат пробел запускаем меню уровней
                if event.key == pygame.K_SPACE:
                    level_menu()
                # если ESCAPE выходим
                if event.key == pygame.K_ESCAPE:
                    running = False

    main_exit()


if __name__ == '__main__':
    main()
