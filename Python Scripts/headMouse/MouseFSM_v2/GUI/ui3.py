# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\settings.ui'
#
# Created: Thu Apr 11 13:57:22 2013
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import createYaml

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(340, 309)
        Dialog.setMinimumSize(QtCore.QSize(0, 0))
        Dialog.setSizeGripEnabled(False)
        self.gestureLabel = QtGui.QLabel(Dialog)
        self.gestureLabel.setGeometry(QtCore.QRect(10, 10, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.gestureLabel.setFont(font)
        self.gestureLabel.setObjectName(_fromUtf8("gestureLabel"))
        self.leftNodButton = QtGui.QPushButton(Dialog)
        self.leftNodButton.setGeometry(QtCore.QRect(10, 40, 91, 51))
        self.leftNodButton.setObjectName(_fromUtf8("leftNodButton"))
        self.rightNodButton = QtGui.QPushButton(Dialog)
        self.rightNodButton.setGeometry(QtCore.QRect(120, 40, 91, 51))
        self.rightNodButton.setObjectName(_fromUtf8("rightNodButton"))
        self.gestureLabel_2 = QtGui.QLabel(Dialog)
        self.gestureLabel_2.setGeometry(QtCore.QRect(20, 110, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.gestureLabel_2.setFont(font)
        self.gestureLabel_2.setObjectName(_fromUtf8("gestureLabel_2"))
        self.plusButton = QtGui.QPushButton(Dialog)
        self.plusButton.setGeometry(QtCore.QRect(10, 140, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.plusButton.setFont(font)
        self.plusButton.setObjectName(_fromUtf8("plusButton"))
        self.minusButton = QtGui.QPushButton(Dialog)
        self.minusButton.setGeometry(QtCore.QRect(120, 140, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.minusButton.setFont(font)
        self.minusButton.setObjectName(_fromUtf8("minusButton"))
        self.lcdDisplay = QtGui.QLCDNumber(Dialog)
        self.lcdDisplay.setGeometry(QtCore.QRect(240, 140, 61, 51))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.lcdDisplay.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lcdDisplay.setFont(font)
        self.lcdDisplay.setFrameShape(QtGui.QFrame.StyledPanel)
        self.lcdDisplay.setFrameShadow(QtGui.QFrame.Plain)
        self.lcdDisplay.setNumDigits(1)
        self.lcdDisplay.setProperty("intValue", 5)
        self.lcdDisplay.setObjectName(_fromUtf8("lcdDisplay"))
        self.line = QtGui.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(0, 210, 341, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.runButton = QtGui.QPushButton(Dialog)
        self.runButton.setGeometry(QtCore.QRect(40, 240, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.runButton.setFont(font)
        self.runButton.setObjectName(_fromUtf8("runButton"))
        self.exitButton = QtGui.QPushButton(Dialog)
        self.exitButton.setGeometry(QtCore.QRect(190, 240, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.exitButton.setFont(font)
        self.exitButton.setObjectName(_fromUtf8("exitButton"))
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(220, 20, 111, 111))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.basicButton = QtGui.QRadioButton(self.groupBox)
        self.basicButton.setGeometry(QtCore.QRect(20, 20, 95, 20))
        self.basicButton.setChecked(True)
        self.basicButton.setObjectName(_fromUtf8("basicButton"))
        self.logButton = QtGui.QRadioButton(self.groupBox)
        self.logButton.setGeometry(QtCore.QRect(20, 50, 95, 20))
        self.logButton.setObjectName(_fromUtf8("logButton"))
        self.joystickButton = QtGui.QRadioButton(self.groupBox)
        self.joystickButton.setGeometry(QtCore.QRect(20, 80, 95, 20))
        self.joystickButton.setObjectName(_fromUtf8("joystickButton"))
        self.retranslateUi(Dialog)

#=============== START BACKUP ===============================
        Dialog.setWindowTitle("Head Mouse Settings")
        readArgs = createYaml.readParameters()
        self.lcdDisplay.setNumDigits(2) 
        self.lcdDisplay.setProperty("intValue", readArgs["alpha"] + 1)
        mode = readArgs['mode']
        if(mode == 0):
            self.basicButton.setChecked(True)
        elif(mode == 1):
            self.logButton.setChecked(True)
        else:
            self.joystickButton.setChecked(True)

        QtCore.QObject.connect(self.plusButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.increaseSensitivity)
        QtCore.QObject.connect(self.minusButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.decreaseSensitivity)
        QtCore.QObject.connect(self.leftNodButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.recordLeftNodTrainingSet)
        QtCore.QObject.connect(self.rightNodButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.recordRightNodTrainingSet)
        QtCore.QObject.connect(self.runButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.toggleStartStop)
        QtCore.QObject.connect(self.exitButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.exitSoftware)
        QtCore.QObject.connect(self.basicButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.radioButtonClick)
        QtCore.QObject.connect(self.logButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.radioButtonClick)
        QtCore.QObject.connect(self.joystickButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.radioButtonClick)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def radioButtonClick(self):
        if(self.basicButton.isChecked()):
            checkedMode = 0
        if(self.logButton.isChecked()):
            checkedMode = 1
        if(self.joystickButton.isChecked()):
            checkedMode = 2
        createYaml.updateParameters(mode = checkedMode)

    def recordLeftNodTrainingSet(self):
         QtGui.QMessageBox.about(self, "Test Box", "Left Nod Clicked")

    def recordRightNodTrainingSet(self):
        QtGui.QMessageBox.about(self, "Test Box", "Right Nod Clicked")

    def decreaseSensitivity(self):
        alphaValue = self.lcdDisplay.intValue()
        if(alphaValue > 1 ):
            alphaValue = alphaValue - 1
            self.lcdDisplay.setProperty("intValue",  alphaValue)
            createYaml.updateParameters(alpha = alphaValue - 1)
        

    def increaseSensitivity(self):
        alphaValue = self.lcdDisplay.intValue()
        readArgs = createYaml.readParameters() 
        if(alphaValue <  len(readArgs['alpha_vals']) ):
            alphaValue = alphaValue + 1
            self.lcdDisplay.setProperty("intValue",  alphaValue)
            createYaml.updateParameters(alpha = alphaValue - 1)

    def toggleStartStop(self):
        QtGui.QMessageBox.about(self, "Test Box", "Start/Stop Clicked")
        if(self.runButton.text() == "Start"):
            self.runButton.setText("Stop")
        else:
            self.runButton.setText("Start")

    def exitSoftware(self):
        QtGui.QApplication.quit()

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Head Mouse Settings", "Head Mouse Settings", None))
        self.gestureLabel.setText(_translate("Dialog", "Gesture Calibration", None))
        self.leftNodButton.setText(_translate("Dialog", "Left Nod", None))
        self.rightNodButton.setText(_translate("Dialog", "Right Nod", None))
        self.gestureLabel_2.setText(_translate("Dialog", "Sensitivity", None))
        self.plusButton.setText(_translate("Dialog", "+", None))
        self.minusButton.setText(_translate("Dialog", "-", None))
        self.runButton.setText(_translate("Dialog", "Start", None))
        self.exitButton.setText(_translate("Dialog", "Exit", None))
        self.groupBox.setTitle(_translate("Dialog", "Mode", None))
        self.basicButton.setText(_translate("Dialog", "Basic", None))
        self.logButton.setText(_translate("Dialog", "Log", None))
        self.joystickButton.setText(_translate("Dialog", "Joystick", None))

