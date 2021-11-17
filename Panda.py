
from direct.showbase.ShowBase import ShowBase
from direct.actor.Actor import Actor
from panda3d.core import KeyboardButton, Point3
import math


class MyApp(ShowBase):
    def __init__(self):
        super().__init__(self)

        self.forward = KeyboardButton.ascii_key('w')
        self.backward = KeyboardButton.ascii_key('s')
        self.turnRight = KeyboardButton.ascii_key('d')
        self.turnLeft = KeyboardButton.ascii_key('a')


        self.scene = self.loader.loadModel("models/environment")   
        self.scene.setScale(0.25, 0.25, 0.25)
        self.scene.setPos(-8, 42, 0)
        self.scene.reparentTo(self.render)

        self.pandaActor = Actor("models/panda-model", {"walk": "models/panda-walk4"})
        self.pandaActor.setScale(0.05, 0.005, 0.05)
        self.pandaActor.reparentTo(self.render)

        mySound = self.loader.loadSfx("musik.ogg") 
        mySound.play()
        mySound.setVolume(.5)
        mySound.setLoop(True)
        mySound.play()

        self.taskMgr.add(self.moveCharacter, "MoveCharacter")

    def moveCharacter(self, task):
        linearSpeed = 0.1
        angularSpeed = 3
        turn = 0
        step = 0
        keypress = base.mouseWatcherNode.is_button_down
        if keypress(self.turnLeft):
            turn = angularSpeed
        if keypress(self.turnRight):
            turn = -angularSpeed
        if keypress(self.forward):
            step = -linearSpeed
        if keypress(self.backward):
            step = linearSpeed
        newH = self.pandaActor.getH() + turn
        self.pandaActor.setHpr(newH, 0, 0)
        targetAngle = self.pandaActor.getH() * math.pi/180
        targetX = math.cos(targetAngle + math.pi/4) - math.sin(targetAngle + math.pi/4)
        targetY = math.sin(targetAngle + math.pi/4) + math.cos(targetAngle + math.pi/4)
        newX = self.pandaActor.getX() + step * targetX
        newY = self.pandaActor.getY() + step * targetX

        self.pandaActor.setFluidPos(newX, newY, 0)
        return task.cont

app = MyApp()
app.run()
