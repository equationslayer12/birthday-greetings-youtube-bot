import sys
import pygame

# CONSTANTS
FPS = 60
WIDTH, HEIGHT = 1200, 900
# COLORS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BACKGROUND_COLOR = BLACK
NAMES_PATH = "../footage/new_names.txt"


def names_generator():
    with open(NAMES_PATH, "r", encoding="utf-8") as names_file:
        for name in names_file:
            yield name[:-1]


def main():
    pygame.init()
    FONT = pygame.font.Font("../SecularOne.ttf", 160)
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    i = 0
    print(i)
    names = names_generator()
    name = f"{i}\n{next(names)[::-1]}"
    textsurface = FONT.render(name, False, WHITE)
    text_rect = textsurface.get_rect()
    text_rect.center = (WIDTH // 2, HEIGHT // 2)

    # Game loop.
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    i += 1
                    print(i)
                    name = f"{i}\n{next(names)[::-1]}"
                    textsurface = FONT.render(name, False, WHITE)
                    text_rect = textsurface.get_rect()
                    text_rect.center = (WIDTH // 2, HEIGHT // 2)
        # Update.

        # Draw.
        screen.fill(BACKGROUND_COLOR)
        screen.blit(textsurface, text_rect)

        pygame.display.update()
        clock.tick(FPS)


if __name__ == '__main__':
    main()
