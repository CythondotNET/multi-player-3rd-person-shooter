from direct.showbase.ShowBase import ShowBase



class MyApp(ShowBase):


    def __init__(self):

        ShowBase.__init__(self)

        self.gun = self.loader.loadModel('M4A4.glb')
        self.gun.reparentTo(self.render)
        self.gun.setScale(1000, 1000, 1000)
        

app = MyApp()
app.run()