"""
This script contains battle field class
"""

START_BATTLE_MSG = 'Battle Started,\nYuan, age:{}, Toefl score: {}, level: {}\nvs\n{}, level: {}'
SEPARATOR_LENGTH = 48
STATUS_MSG = 'Yuan: **HP**: {}, **ATK**: {}\n\n{}: **HP**: {}, **ATK**:{}\n'


class BattleField:

    def __init__(self, yuan, enemy):
        self.yuan = yuan
        self.enemy = enemy

    def start(self):
        """
        Start battle.
        """
        print(START_BATTLE_MSG.format(self.yuan.age, self.yuan.toefl, self.yuan._level, self.enemy.name, self.enemy.level))
        print('*'*SEPARATOR_LENGTH)
        print(STATUS_MSG.format(self.yuan.hp, self.yuan.attack_point, self.enemy.name, self.enemy.hp, self.enemy.attack_point))

    def fight(self):
        """
        Fight between yuan and enemy
        @return <bool> victory
        """
        flag = True
        victory = None
        while flag:
            choice = input('Yuan: plz tell me what to do: (a: attack, b: talk, c: answer question\n').lower()
            if choice == 'a':
                print('Yuan attacking\n')
                self.enemy.get_attacked(self.yuan.attack_point)
            elif choice == 'b':
                print('Yuan talking\n')
                self.yuan.talk()
            elif choice == 'c':
                print('Yuan asking enemy to ask a question...\n')
                self.yuan.answer()
            else:
                print('Yuan Panicked')
            enemy_action = self.enemy.take_action()
            if enemy_action == 1:
                print('enemy attacking, attack point: {}'.format(self.enemy.attack_point))
                self.yuan.get_attacked(self.enemy.attack_point)
            if self.enemy.hp <= 0:
                print('Yuan defeated {}'.format(self.enemy.name))
                flag = False
                victory = True
            if self.yuan.hp <= 0:
                self.yuan.die()
                flag = False
                victory = False

        return victory
