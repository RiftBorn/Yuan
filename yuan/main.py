from common.game import Game


def run():
	game = Game()
	game.start()
	shen = game.generate_enemy('Muy Shen', 10)
	game.battle(shen)


if __name__ == "__main__":
	run()
