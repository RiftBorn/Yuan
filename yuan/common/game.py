"""
This script is a game generator
"""
from .battle_field import BattleField
from .enemy import Enemy
from .game_panel import GamePanel
import random
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

    def main(self):
        """
        Main program
        """
        self.start()
        flag = True
        game_panel = GamePanel(self.yuan)
        while flag:
            choice = game_panel.show_and_take_input()
            choice_chart = {
                "a": self.battle,
                "b": self.yuan.rest,
                "c": self.yuan.talk,
                "d": self.yuan.print_status,
                "q": "quit",
            }
            item = choice_chart.get(choice)
            if item is None:
                print('?')
            elif item == 'quit':
                flag = False
            elif '.battle' in str(item):
                item(self.generate_enemy())
            else:
                item()
        print("Game Over...Please play again")

    def start(self):
        print('Starting game...')
        pass

    @staticmethod
    def generate_enemy(name=None, level=None):
        """
        generate enemy by name and level
        @return: enemy object
        """
        if name is None :
            random.seed()
            name_code = random.randint(0, 99999)
            name = 'Enemy ' + str(name_code)
        if level is None:
            level = random.randint(1, 20)
        return Enemy(name, level)
