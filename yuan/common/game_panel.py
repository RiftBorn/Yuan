"""
Game Panel class
"""


PANEL = """--------------------------------------------------------
                /\\
             //\\\\//\\\\    __________________________
             [(*)(*)]   <Please tell me what to do:>
             [  v   ]   <a. Next Fight    b. Rest   > 
             d       b  <c. Talk Shit     d. Status >
              L  .  J    --------------------------
              |  || |
              |  || |
              L__IL_I                        q. Quit
---------------------------------------------------------\n
"""


class GamePanel:

    def __init__(self, yuan):
        """
        Constructor of game panel class
        @param yuan: <YuanLi> object
        """
        self.yuan = yuan

    def show_and_take_input(self):
        """
        Shows the panel and wait for user input
        """
        return input(PANEL)
