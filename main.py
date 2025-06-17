from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from math import pi, sin, cos


class MyApp(ShowBase):


    def __init__(self):
            
        ShowBase.__init__(self)


        self.gun = self.loader.loadModel('M4A4.glb')
        self.gun.reparentTo(self.render)
        self.gun.setScale(500, 500, 500)
        self.gun.setPos(-4, 3, 3)
        self.taskMgr.add(self.spinCameraTask, "SpinCamraTask")
        
    def spinCameraTask(self, task):

        angleDegrees = task.time * 20

        angleRadians = angleDegrees * (pi / 180.0)

        self.camera.setPos(20 * sin(angleRadians) - 2, (-20 * cos(angleRadians)) + 10, 3)

        self.camera.setHpr(angleDegrees, 0, 0)

        return Task.cont
        

app = MyApp()
app.run()