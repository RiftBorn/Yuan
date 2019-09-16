from common.yuan_li import YuanLi


def run():
	yuan = YuanLi()
	yuan.talk()
	yuan.get_attention()
	yuan.answer()
	yuan.fight()
	print("Yuan's level is: ",  yuan._level)

if __name__ == "__main__":
	run()

