"""
Enemy class
"""
import random


class Enemy:

    def __init__(self, name='random guy', level: int = 1):
        self.name = name
        self.level = level
        self.hp = self.compute_init_hp()
        self.attack_point = self.compute_init_attack()

    def compute_init_hp(self):
        random.seed()
        return 17 + (self.level/5)**random.randint(0, 5)

    def compute_init_attack(self):
        random.seed()
        return 18 + (self.level/8)**random.randint(0, 5)

    def get_attacked(self, attack_point):
        self.hp -= attack_point

    def take_action(self):
        random.seed()
        randomed = random.randint(0, 10)
        if randomed < 3:
            self.talk()
            return 0
        else:
            return 1

    def talk(self):
        print('{}: Yuan? Yuan~~~~~'.format(self.name))
