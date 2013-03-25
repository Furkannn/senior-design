#!/usr/bin/python
from pymouse import PyMouse

class HostDeviceClass:

  def __init__(self):
    self.m = PyMouse()
    self.screen = ScreenClass(self.m.screen_size()[0], self.m.screen_size()[1])
    self.cursor = CursorClass(self.screen.width/2, self.screen.height/2)

  def centerCursor(self):
    self.cursor = CursorClass(self.screen.width/2, self.screen.height/2)
    print "Updated Cursor Position to center of screen (" + str(self.cursor.x) + ", " + str(self.cursor.y) + ")."
    self.moveCursor()

  def moveCursor(self):
    self.m.move(self.cursor.x, self.cursor.y)

  def displaceCursor(self, disp):
    # update cursor
    self.cursor.x = self.cursor.x + disp.x
    self.cursor.y = self.cursor.y + disp.y

    # screen limits
    if self.cursor.x > self.screen.width:
      self.cursor.x = self.screen.width
    if self.cursor.x < 0:
      self.cursor.x = 0
    if self.cursor.y > self.screen.height:
      self.cursor.y = self.screen.height
    if self.cursor.y < 0:
      self.cursor.y = 0
    self.moveCursor()


class CursorClass:

  def __init__(self, x, y):
    self.x = x
    self.y = y
    
class ScreenClass:

  def __init__(self, width, height):
    self.width = width
    self.height = height
    
