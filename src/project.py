import pygame


def main():
    pygame.init()
    pygame.display.set_caption("Underwater World")
    resolution = (768, 432)
    screen = pygame.display.set_mode(resolution)

    running = True
    while running:
        # Event Loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

        # Game Logic

        # Render & Display
        gray = (50, 50, 50)
        screen.fill((gray))
        pygame.display.flip()
    pygame.quit()

if __name__ == "__main__":
    main()