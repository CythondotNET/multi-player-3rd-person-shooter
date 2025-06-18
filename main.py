from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from math import pi, sin, cos

speed = 100.0
y_delta = 0
x_delta = 0

class MyApp(ShowBase):

    def __init__(self):
            
        ShowBase.__init__(self)
        # Load the environment model.

        self.scene = self.loader.loadModel("models/environment")

        # Reparent the model to render.

        self.scene.reparentTo(self.render)

        # Apply scale and position transforms on the model.

        self.scene.setScale(0.25, 0.25, 0.25)

        self.scene.setPos(-8, 42, 0)

        base.disableMouse()
        self.gun = self.loader.loadModel('M4A4.glb')
        self.gun.reparentTo(self.render)
        self.gun.setScale(500, 500, 500)
        self.gun.setPos(0, 0, 0)
        self.camera.setPos(self.gun.getX() - 0.4, self.gun.getY() - 5, self.gun.getZ() + 8)
        self.camera.setP(-15)
        self.gun.setR(-90)
        base.buttonThrowers[0].node().setKeystrokeEvent('keystroke')
        self.accept("keystroke", self.move)

    def move(self, keyname):
        global y_delta, x_delta
        if keyname == "w":
            y_delta = (speed * globalClock.get_dt())
        if keyname == "s":
            y_delta = ((speed * globalClock.get_dt()) * -1)
        y_delta += self.gun.getY()
        self.gun.setY(y_delta)
        y_delta = 0
        if keyname == "d":
            x_delta = (speed * globalClock.get_dt())
        if keyname == "a":
            x_delta = ((speed * globalClock.get_dt()) * -1)
        x_delta += self.gun.getX()
        self.gun.setX(x_delta)
        x_delta = 0
        self.camera.setPos(self.gun.getX() - 0.4, self.gun.getY() - 5, self.gun.getZ() + 8)
app = MyApp()
app.run()