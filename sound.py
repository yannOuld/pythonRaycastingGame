import pygame as pg

class Sound:
    def __init__(self, game):
        self.game = game
        pg.mixer.init()
        self.path = 'ressources/sound/'
        self.crowbar = pg.mixer.Sound(self.path + 'crowbar.wav')
        self.npc_pain = pg.mixer.Sound(self.path + 'npc_pain.wav')
        self.player_pain = pg.mixer.Sound(self.path + 'player_pain.wav')
        self.npc_death = pg.mixer.Sound(self.path + 'npc_death.wav')
        self.npc_shot = pg.mixer.Sound(self.path + 'npc_attack.wav')
        self.shotgun = pg.mixer.Sound(self.path + 'shotgun.wav')
        self.theme= pg.mixer.music.load(self.path + 'theme.mp3')
        self.theme = pg.mixer.music.load(self.path + 'theme.mp3')
