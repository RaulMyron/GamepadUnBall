import cairo
import numpy as np

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class Field:
    width = 1.7
    height = 1.3

    def __init__(self):
        pass
        
    def enterCoordinateSystem(self, drawingArea: Gtk.DrawingArea, context: cairo.Context):
        context.save()

        width = drawingArea.get_allocated_width()
        height = drawingArea.get_allocated_height()

        # Change coordinate system
        ratio = Field.width / Field.height
        context.translate(width / 2, height / 2)
        if width / height <= ratio:
            fieldHeight = width / ratio
            context.scale(width / Field.width, fieldHeight / Field.height)
        else:
            fieldWidth = height * ratio
            context.scale(fieldWidth / Field.width, height / Field.height)

    def draw(self, drawingArea: Gtk.DrawingArea, context: cairo.Context):
        # Style
        context.set_source_rgba(1, 1, 1, 0.6)
        context.set_line_width(context.device_to_user_distance(2, 2)[0])

        # Larger rectangle
        context.rectangle(-1.5/2, -1.3/2, 1.5, 1.3)

        # Goal
        context.rectangle(-1.5/2-0.1, -0.4/2, 0.1, 0.4)
        context.rectangle(1.5/2, -0.4/2, 0.1, 0.4)

        # Area
        context.rectangle(-1.5/2, -0.7/2, 0.15, 0.7)
        context.rectangle(1.5/2-0.15, -0.7/2, 0.15, 0.7)

        # Draw
        context.stroke()

        # Center
        context.arc(0, 0, 0.2, 0, 2*np.pi)

        # Center line
        context.move_to(0, -1.3/2)
        context.line_to(0, 1.3/2)

        # Draw
        context.stroke()