import pygame


class LoadSprite():
    def __init__(self, image):
        self.sheet = image

    def load_sheet(self, frame, width, height):
        image = pygame.Surface((width, height))
        image.blit(self.sheet, (0, 0), frame*width, 0, width, height)
        black = (0, 0, 0)
        # Creates Transparent Background
        image.set_colorkey(black)
        return image

class CharacterAnim():
    def __init__(self):
        self.sprite_imgs = pygame.image.load('img/char_sprite.png').convert_alpha()
        self.char_sheet = LoadSprite(self.sprite_imgs)
        self.anim_frames = [4, 4, 4]
        self.anim_list = []
        self.frame = 0
        self.action = 0
        self.last_update = pygame.time.get_ticks()
        # Creates the animation list for each step
        counter = 0
        for animation in self.anim_frames:
            loop_list = []
            for _ in range(animation):
                loop_list.append(self.char_sheet.load_sheet(counter, 100, 100))
                counter += 1
            self.anim_list.append(loop_list)
        self.image = self.anim_list[self.action][self.frame]

    def update_anim(self):
        anim_cd = 150
        self.image = self.anim_list[self.action][self.frame]
        if pygame.time.get_ticks() - self.last_update > anim_cd:
            self.last_update = pygame.time.get_ticks()
            self.frame += 1
        if self.frame >= len(self.anim_list[self.action]):
            self.frame = 0

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