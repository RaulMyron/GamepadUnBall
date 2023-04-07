import cairo
import numpy as np
from .field import Field
from .vectorField import VectorField
from .robot import Robot

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

def F(xx, yy):
    return np.zeros_like(xx)#np.arctan2(xx, yy) + np.arctan2(yy, -xx)

class Drawer:
    def __init__(self, drawingArea: Gtk.DrawingArea):
        self.drawingArea = drawingArea
        self.field = Field()
        self.vectorField = VectorField(F)
        self.robots = [
            Robot("0", lambda: (0,0,np.pi/4), 'yellow'),
            Robot("1", lambda: (0.5,0,np.pi/6), 'yellow'),
            Robot("2", lambda: (0,0.5,np.pi), 'yellow'),
            Robot("0", lambda: (-0.5,0,-np.pi/2), 'blue'),
            Robot("1", lambda: (-0.5,0,np.pi), 'blue'),
            Robot("2", lambda: (0.5,0.5,np.pi/6), 'blue'),
        ]

        self.drawingArea.connect("draw", self.onDraw)

    def onDraw(self, drawingArea: Gtk.DrawingArea, context: cairo.Context):
        self.field.enterCoordinateSystem(drawingArea, context)

        self.field.draw(drawingArea, context)
        self.vectorField.draw(drawingArea, context)
        for robot in self.robots: robot.draw(drawingArea, context)
    