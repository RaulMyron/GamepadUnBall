import cairo
import numpy as np
from . import Field

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class VectorField:
    def __init__(self, vectorFieldProvider):
        self.vectorFieldProvider = vectorFieldProvider

    def compute(self):
        x = np.linspace(-Field.width/2,  Field.width/2,  30)
        y = np.linspace(-Field.height/2, Field.height/2, 30)
        xx, yy = np.meshgrid(x,y)
        return xx, yy, self.vectorFieldProvider(xx, yy)

    def computeArrows(self, angles, length: float, head_angle: float, head_length: float):
        lt1x = length * np.cos(-angles)
        lt1y = length * np.sin(-angles)
        mt1x = -head_length * np.cos(-angles - head_angle)
        mt1y = -head_length * np.sin(-angles - head_angle)
        rlt1x = -mt1x
        rlt1y = -mt1y
        rlt2x = -head_length * np.cos(-angles + head_angle)
        rlt2y = -head_length * np.sin(-angles + head_angle)

        return lt1x, lt1y, mt1x, mt1y, rlt1x, rlt1y, rlt2x, rlt2y

    def drawArrow(self, context: cairo.Context, lt1x, lt1y, mt1x, mt1y, rlt1x, rlt1y, rlt2x, rlt2y):
        context.rel_line_to(lt1x, lt1y)
        context.rel_move_to(mt1x, mt1y)
        context.rel_line_to(rlt1x, rlt1y)
        context.rel_line_to(rlt2x, rlt2y)

    def draw(self, drawingArea: Gtk.DrawingArea, context: cairo.Context):
        # Style
        context.set_source_rgba(1, 1, 1, 0.1)
        context.set_line_width(context.device_to_user_distance(2, 2)[0])

        # Arrows
        xx, yy, angles = self.compute()
        lt1x, lt1y, mt1x, mt1y, rlt1x, rlt1y, rlt2x, rlt2y = self.computeArrows(angles, 0.05, np.pi/6, 0.02)
        for i in range(xx.shape[0]):
            for j in range(yy.shape[1]):
                context.move_to(xx[i][j], yy[i][j])
                self.drawArrow(context, lt1x[i][j], lt1y[i][j], mt1x[i][j], mt1y[i][j], rlt1x[i][j], rlt1y[i][j], rlt2x[i][j], rlt2y[i][j])

        context.stroke()