from sprite_object import *


class Weapon(AnimatedSprite):
    def __init__(self, game, path='ressources/textures/sprites/weapon/gun/1.png', scale=0.4, animated_time=90):
        super().__init__(game=game, path=path, scale=scale, animated_time=animated_time)
        self.image = deque(
            [pg.transform.smoothscale(img, (self.image.get_width() * scale, self.image.get_height() * scale))
             for img in self.images])
        self.weapon_pos = (HALF_WIDTH + self.images[0].get_width() // 2, HEIGHT - self.images[0].get_height())
        self.reloading = False
        self.num_images = len(self.images)
        self.frame_counter = 0
        self.damage = 20

    def animate_attack(self):
        if self.reloading:
            self.game.player.attack = False
            if self.animation_trigger:
                self.images.rotate(-1)
                self.frame_counter += 1
                if self.frame_counter == self.num_images:
                    self.reloading = False
                    self.frame_counter = 0

    def draw(self):
        self.game.screen.blit(self.images[0], self.weapon_pos)

    def update(self):
        self.check_animation_time()
        self.animate_attack()