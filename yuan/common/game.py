"""
This script is a game generator
"""
from .battle_field import BattleField
from .enemy import Enemy
from .yuan_li import YuanLi


class Game:

    def __init__(self):
        self.yuan = YuanLi()
        pass

    def battle(self, enemy):
        battle_field = BattleField(self.yuan, enemy)
        battle_field.start()
        victory = battle_field.fight()
        if victory:
            print('Yuan won the battle! level up...')
            self.yuan.level_up()
            print('Yuan is now level {}'.format(self.yuan._level))

    def encounter(self):
        pass

    def start(self):
        print('Starting game...')
        pass

    def generate_enemy(self, name=None, level=None):
        """
        generate enemy by name and level
        @return: enemy object
        """
        return Enemy(name, level)
