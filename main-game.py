from direct.showbase.ShowBase import ShowBase
from panda3d.core import WindowProperties
from direct.actor.Actor import Actor

class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        # Requesting that the window's resolution be (1000, 750)

        properties = WindowProperties()
        properties.setSize(640, 480)
        self.win.requestProperties(properties)

        # Disabling the mouse camera.
        self.disableMouse()

        # Creating the environment model.
        self.environment = loader.loadModel("PandaSampleModels/Environment/environment")
        self.environment.reparentTo(render)

        # Creating the Actor with a model and a walk animation.
        self.tempActor = Actor("models/act_p3d_chan", 
        {
            "walk": "models/a_p3d_chan_walk.egg"
        })

        self.tempActor.reparentTo(render)
        self.tempActor.getChild(0).setH(180)
        self.tempActor.loop("walk")

        # Move the camera to a position high above the screen
        # -- that is, offset it along the z-axis
        self.camera.setPos(0,0,32)
        # Tilt the camera down by setting its pitch (the p in hpr)
        self.camera.setP(-90)



game = Game()
game.run()