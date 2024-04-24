import pygame


class LoadSprite():
    def __init__(self, image):
        self.sheet = image

    def load_sheet(self, frame, width, height):
        image = pygame.Surface((width, height))
        image.blit(self.sheet, (0, 0), (frame*width, 0, width, height))
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

    def update_action(self, new_action):
        if new_action != self.action:
            self.action = new_action
            self.frame = 0
            self.last_update = pygame.time.get_ticks()

    def draw(self, surface):
        surface.blit(self.image, (0, 0))

class MakeBackground():
    def __init__(self):
        self.image_list = self.load_images()
        self.scroll = 0

    def load_images(self):
        bg_images = []
        for i in range(1, 5):
            bg_image = pygame.image.load(f"img/bg_layer{i}.png")
            bg_images.append(bg_image)
        return bg_images
    
    def draw_bg(self, surface):
        for x in range(4):
            for img in self.image_list:
                surface.blit(img, ((x * 768) - self.scroll, 0))
    
    def create_loop(self):
        # Moves the background
        if pygame.key.get_pressed()[pygame.K_LEFT] and self.scroll > 0:
            self.scroll -= 5
        elif pygame.key.get_pressed()[pygame.K_RIGHT] and self.scroll < 1000:
            self.scroll += 5

def main():
    pygame.init()
    pygame.display.set_caption("Underwater World")
    resolution = (768, 432)
    screen = pygame.display.set_mode(resolution)
    character = CharacterAnim()
    background = MakeBackground()

    running = True
    while running:
        # Event Loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

            # Character Direction Changes
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                character.update_action(0)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                character.update_action(1)
            else:
                character.update_action(2)

        # Game Logic
        character.update_anim()
        background.create_loop()
        # Render & Display
        background.draw_bg(screen)
        character.draw(screen)
        pygame.display.flip()
    pygame.quit()

if __name__ == "__main__":
    main()