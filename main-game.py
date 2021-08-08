from direct.showbase.ShowBase import ShowBase
from panda3d.core import WindowProperties
from panda3d.core import AmbientLight
from panda3d.core import Vec4, Vec3
from panda3d.core import DirectionalLight
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

        ambientLight = AmbientLight("ambient light")
        ambientLight.setColor(Vec4(0.2, 0.2, 0.2, 1))
        # Did this to get the node path since we created a node right above.
        self.ambientLightNodePath = render.attachNewNode(ambientLight)
        render.setLight(self.ambientLightNodePath)

        mainLight = DirectionalLight("main light")
        # Same thing here.
        self.mainLightNodePath = render.attachNewNode(mainLight)
        # Turn by 45 degrees, then tilt down by 45.
        self.mainLightNodePath.setHpr(45, -45, 0)
        render.setLight(self.mainLightNodePath)

        # Applying a shader
        render.setShaderAuto()

        self.keyMap = {
            "up": False,
            "down": False,
            "left": False,
            "right": False,
            "shoot": False
        }
               
        self.accept("w", self.updateKeyMap, ["up", True])
        self.accept("w-up", self.updateKeyMap, ["up", False])
        self.accept("s", self.updateKeyMap, ["down", True])
        self.accept("s-up", self.updateKeyMap, ["down", False])
        self.accept("a", self.updateKeyMap, ["left", True])
        self.accept("a-up", self.updateKeyMap, ["left", False])
        self.accept("d", self.updateKeyMap, ["right", True])
        self.accept("d-up", self.updateKeyMap, ["right", False])
        self.accept("mouse1", self.updateKeyMap, ["shoot", True])
        self.accept("mouse1-up", self.updateKeyMap, ["shoot", False])

        # Task manager code.

        self.updateTask = taskMgr.add(self.update, "update")

    def update(self, task):
        dt = globalClock.getDt()

        # Use the global time to calculate how much we move.

        if self.keyMap["up"]:
            self.tempActor.setPos(self.tempActor.getPos() + Vec3(0, 5.0*dt, 0))
        if self.keyMap["down"]:
            self.tempActor.setPos(self.tempActor.getPos() + Vec3(0, -5.0*dt, 0))
        if self.keyMap["left"]:
            self.tempActor.setPos(self.tempActor.getPos() + Vec3(-5.0*dt, 0, 0))
        if self.keyMap["right"]:
            self.tempActor.setPos(self.tempActor.getPos() + Vec3(5.0*dt, 0, 0))
        if self.keyMap["shoot"]:
            print("Zap!")

        return task.cont
        
    def updateKeyMap(self, controlName, controlState):
            self.keyMap[controlName] = controlState
            print(f"{controlName} set to {controlState}")

game = Game()
game.run()