#!/usr/bin/python
from pymouse import PyMouse
import HelperClasses

class HostDeviceClass:

  def __init__(self):
    self.m = PyMouse()
    self.screen = HelperClasses.ScreenClass(self.m.screen_size()[0], self.m.screen_size()[1])
    self.cursor = HelperClasses.CursorClass(self.screen.width/2, self.screen.height/2)

  def moveCursorToCenter(self):
    self.cursor = HelperClasses.CursorClass(self.screen.width/2, self.screen.height/2)
    print "Updated Cursor Position to center of screen (" + str(self.cursor.x) + ", " + str(self.cursor.y) + ")."
    self.moveCursor()

  def moveCursor(self):
    self.m.move(self.cursor.x, self.cursor.y)

  def mousePress(self):
    print "PRESS"
    self.m.press(self.cursor.x, self.cursor.y)

  def mouseRelease(self):
    print "RELEASE"
    self.m.release(self.cursor.x, self.cursor.y)

  def displaceCursor(self, disp):
    # update cursor
    new_x = self.cursor.x + disp.x
    new_y = self.cursor.y + disp.y

    # screen limits
    if new_x > self.screen.width:
      new_x = self.screen.width
    if new_x < 0:
      new_x = 0
    if new_y > self.screen.height:
      new_y = self.screen.height
    if new_y < 0:
      new_y = 0

    actualMovement = HelperClasses.CursorClass(self.cursor.x - new_x, self.cursor.y - new_y)

    self.cursor.x = new_x
    self.cursor.y = new_y
    self.moveCursor()

    return actualMovement

    
