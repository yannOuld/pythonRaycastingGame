from sprite_object import *
from npc import *


class ObjectHandler:
    def __init__(self, game):
        self.game = game
        self.sprite_list = []
        self.npc_list = []
        self.npc_sprite_path = 'ressources/textures/npc/'
        self.static_sprite_path = 'ressources/textures/sprites/static/'
        self.anim_sprite_path = 'ressources/textures/sprites/animated'
        add_sprite = self.add_sprite
        add_npc = self.add_npc
        self.npc_positions = {}

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
        add_sprite(AnimatedSprite(game, pos=(9.5, 1.5)))
        add_sprite(AnimatedSprite(game, pos=(14.5, 1.5)))

        # npc enemies
        add_npc(CyberDemonNPC(game, pos=(8, 19.5)))
        add_npc(SoldierNPC(game, pos=(12.5, 5.5)))
        add_npc(SoldierNPC(game, pos=(4, 21)))
        add_npc(SoldierNPC(game, pos=(11.5, 5.5)))
        add_npc(SoldierNPC(game, pos=(14, 24)))
        add_npc(CacoDemonNPC(game, pos=(3.5, 19)))

    def update(self):
        self.npc_positions = {npc.map_pos for npc in self.npc_list if npc.alive}
        [sprite.update() for sprite in self.sprite_list]
        [npc.update() for npc in self.npc_list]

    def add_npc(self, npc):
        self.npc_list.append(npc)

    def add_sprite(self, sprite):
        self.sprite_list.append(sprite)