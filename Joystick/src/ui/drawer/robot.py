import cairo
import numpy as np
from . import Field

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class Robot:
    def __init__(self, name, poseProvider, color='yellow'):
        self.name = name
        self.poseProvider = poseProvider
        self.robotColor = {'blue': (0.2, 0.3, 1), 'yellow': (1, 1, 0)}[color]

    def draw(self, drawingArea: Gtk.DrawingArea, context: cairo.Context):
        # Style
        context.set_line_width(context.device_to_user_distance(3,3)[0])

        # Robot
        x, y, th = self.poseProvider()
        
        context.save()
        context.translate(x,y)
        context.rotate(th)

        context.set_source_rgb(*self.robotColor)
        context.rectangle(-0.08/2, -0.08/2, 0.08, 0.08)
        context.fill()

        context.set_source_rgb(0, 0, 0)
        context.rectangle(-0.08/2, -0.08/2, 0.08, 0.08)
        context.stroke()

        context.restore()

        context.save()
        context.translate(x,y)
        context.set_source_rgb(0, 0, 0)
        context.select_font_face("Arial", cairo.FONT_SLANT_NORMAL,  cairo.FONT_WEIGHT_NORMAL)
        context.set_font_size(0.07)
        (x, y, width, height, dx, dy) = context.text_extents("0")
        context.move_to(-width/2, height/2)    
        context.show_text(self.name)
        context.stroke()
        context.restore()