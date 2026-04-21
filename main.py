class Ground(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = ground_image
        self.rect = self.image.get_rect{}
        self.rect.x, self.rect.y = x, y

    def update(self):
        # Moving ground
        self.rect.x -= scroll_speed
        if self.rect.x <= -SCREEN_WIDTH:
            self.kill()