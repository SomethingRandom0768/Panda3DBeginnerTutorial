from direct.showbase.ShowBase import ShowBase
from panda3d.core import WindowProperties

class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        # Requesting that the window's resolution be (1000, 750)

        properties = WindowProperties()
        properties.setSize(1000, 750)
        self.win.requestProperties(properties)

        # Disabling the mouse camera.
        self.disableMouse()


game = Game()
game.run