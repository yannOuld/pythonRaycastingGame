from sprite_object import *
from npc import *
from random import choices, randrange

class ObjectHandler:
    def __init__(self, game):
        self.game = game
        self.sprite_list = []
        self.npc_list = []
        self.npc_sprite_path = 'ressources/textures/npc/'
        self.static_sprite_path = 'ressources/textures/sprites/static/'
        self.anim_sprite_path = 'ressources/textures/sprites/animated'
        add_sprite = self.add_sprite
        # add_npc = self.add_npc
        self.npc_positions = {}
        self.enemies = 15
        self.npc_types = [SoldierNPC, CacoDemonNPC, CyberDemonNPC]
        self.weights = [70, 20, 10]
        self.restricted_area = {(i, j) for i in range(10) for j in range(10)}
        self.spawn_npc()

        # decorative sprites
        add_sprite(SpriteObject(game, pos=(11.5, 13.5)))
        add_sprite(SpriteObject(game, pos=(14.5, 13.5)))
        add_sprite(SpriteObject(game, path='ressources/textures/sprites/static/barrel.png', pos=(1.5, 10.5)))
        add_sprite(SpriteObject(game, path='ressources/textures/sprites/static/barrel_2.png', pos=(5.5, 15.5)))
        add_sprite(SpriteObject(game, path='ressources/textures/sprites/static/barrel_3.png', pos=(6, 15.5)))
        add_sprite(SpriteObject(game, path='ressources/textures/sprites/static/plant.png', pos=(14, 24.5)))
        add_sprite(SpriteObject(game, path='ressources/textures/sprites/static/plant.png', pos=(7.5, 7)))
        add_sprite(AnimatedSprite(game, pos=(3.5, 22.5)))
        add_sprite(AnimatedSprite(game, pos=(3.5, 24.5)))
        add_sprite(AnimatedSprite(game, pos=(7, 51.5)))
        add_sprite(AnimatedSprite(game, pos=(9, 51.5)))

    def spawn_npc(self):
        for i in range(self.enemies):
            npc = choices(self.npc_types, self.weights)[0]
            pos = x, y = randrange(self.game.map.cols), randrange(self.game.map.rows)
            while (pos in self.game.map.world_map) or (pos in self.restricted_area):
                pos = x, y = randrange(self.game.map.cols), randrange(self.game.map.rows)
            self.add_npc(npc(self.game, pos=(x + 0.5, y + 0.5)))

    def check_win(self):
        if not len(self.npc_positions):
            self.game.object_renderer.win()
            pg.display.flip()
            pg.time.delay(1500)
            self.game.new_game()

    def update(self):
        self.npc_positions = {npc.map_pos for npc in self.npc_list if npc.alive}
        [sprite.update() for sprite in self.sprite_list]
        [npc.update() for npc in self.npc_list]
        self.check_win()

    def add_npc(self, npc):
        self.npc_list.append(npc)

    def add_sprite(self, sprite):
        self.sprite_list.append(sprite)