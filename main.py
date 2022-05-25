from object3D import *
from camera import *
from projection import *
import pygame as pg

class SoftwareRender:
    def __init__(self):
        pg.init()
        self.RES = self.WIDTH, self.HEIGHT = 950, 530
        self.H_WIDTH, self.H_HEIGHT = self.WIDTH // 2, self.HEIGHT // 2 
        self.FPS = 60
        self.screen = pg.display.set_mode(self.RES)
        self.clock = pg.time.Clock()
        self.createObject()

    def createObject(self):
        self.camera = Camera(self, [-5, 5, -50])
        self.projection = Projection(self)
        self.object = self.getObjectFromFile('resources/tank.obj')

        #### create cube
        # self.object = Object3D(self)
        # self.object.translate([0.2, 0.4, 0.2])
        # self.axes = Axes(self)
        # self.axes.translate([0.7, 0.9, 0.7])
        # self.world_axes = Axes(self)
        # self.world_axes.movement_flag = False
        # self.world_axes.scale(2.5)
        # self.world_axes.translate([0.0001, 0.0001, 0.0001])

    def getObjectFromFile(self, filename):
        vertex, faces = [], []
        with open(filename) as f:
            for line in f:
                if line.startswith('v '):
                    vertex.append([float(i) for i in line.split()[1:]] + [1])
                elif line.startswith('f'):
                    faces_ = line.split()[1:]
                    faces.append([int(face_.split('/')[0]) -1 for face_ in faces_])
        return Object3D(self, vertex, faces)

    def draw(self):
        self.screen.fill(pg.Color('darkslategray'))
        # self.world_axes.draw()
        # self.axes.draw()
        self.object.draw()
    
    def run(self):
        while True:
            self.draw()
            self.camera.control()
            [exit() for i in pg.event.get() if i.type == pg.QUIT]
            pg.display.set_caption(str(self.clock.get_fps()))
            pg.display.flip()
            self.clock.tick(self.FPS)

if __name__ == '__main__':
    app = SoftwareRender()
    app.run()