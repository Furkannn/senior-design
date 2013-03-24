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

  def moveCursor(self):
    self.m.move(self.cursor.x, self.cursor.y)




class CursorClass:

  def __init__(self, x, y):
    self.x = x
    self.y = y
    
class ScreenClass:

  def __init__(self, width, height):
    self.width = width
    self.height = height
    
