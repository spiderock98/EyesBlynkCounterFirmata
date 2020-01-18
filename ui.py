# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(617, 729)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnStart = QtWidgets.QPushButton(self.centralwidget)
        self.btnStart.setGeometry(QtCore.QRect(420, 150, 111, 25))
        self.btnStart.setObjectName("btnStart")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(10, 190, 591, 41))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.spinEye = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.spinEye.setGeometry(QtCore.QRect(150, 15, 69, 31))
        self.spinEye.setAccelerated(False)
        self.spinEye.setMaximum(0.5)
        self.spinEye.setSingleStep(0.01)
        self.spinEye.setProperty("value", 0.24)
        self.spinEye.setObjectName("spinEye")
        self.lbEyeThread = QtWidgets.QLabel(self.centralwidget)
        self.lbEyeThread.setGeometry(QtCore.QRect(20, 20, 121, 21))
        self.lbEyeThread.setObjectName("lbEyeThread")
        self.lbMouthThread = QtWidgets.QLabel(self.centralwidget)
        self.lbMouthThread.setGeometry(QtCore.QRect(10, 60, 131, 31))
        self.lbMouthThread.setObjectName("lbMouthThread")
        self.spinMouth = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.spinMouth.setGeometry(QtCore.QRect(150, 60, 69, 31))
        self.spinMouth.setMaximum(0.5)
        self.spinMouth.setSingleStep(0.01)
        self.spinMouth.setProperty("value", 0.27)
        self.spinMouth.setObjectName("spinMouth")
        self.slideEye = QtWidgets.QSlider(self.centralwidget)
        self.slideEye.setGeometry(QtCore.QRect(390, 60, 160, 21))
        self.slideEye.setMaximum(50)
        self.slideEye.setSliderPosition(0)
        self.slideEye.setOrientation(QtCore.Qt.Horizontal)
        self.slideEye.setObjectName("slideEye")
        self.lbEyeFrame = QtWidgets.QLabel(self.centralwidget)
        self.lbEyeFrame.setGeometry(QtCore.QRect(260, 60, 121, 17))
        self.lbEyeFrame.setObjectName("lbEyeFrame")
        self.lbMouthFrame = QtWidgets.QLabel(self.centralwidget)
        self.lbMouthFrame.setGeometry(QtCore.QRect(260, 100, 121, 21))
        self.lbMouthFrame.setObjectName("lbMouthFrame")
        self.slideMouth = QtWidgets.QSlider(self.centralwidget)
        self.slideMouth.setGeometry(QtCore.QRect(390, 100, 160, 21))
        self.slideMouth.setMaximum(50)
        self.slideMouth.setOrientation(QtCore.Qt.Horizontal)
        self.slideMouth.setObjectName("slideMouth")
        self.comboSource = QtWidgets.QComboBox(self.centralwidget)
        self.comboSource.setGeometry(QtCore.QRect(390, 20, 91, 21))
        self.comboSource.setObjectName("comboSource")
        self.lbCam = QtWidgets.QLabel(self.centralwidget)
        self.lbCam.setGeometry(QtCore.QRect(260, 20, 121, 20))
        self.lbCam.setObjectName("lbCam")
        self.checkShow = QtWidgets.QCheckBox(self.centralwidget)
        self.checkShow.setGeometry(QtCore.QRect(20, 150, 171, 21))
        self.checkShow.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.checkShow.setObjectName("checkShow")
        self.lbEyeNum = QtWidgets.QLabel(self.centralwidget)
        self.lbEyeNum.setGeometry(QtCore.QRect(560, 60, 67, 21))
        self.lbEyeNum.setObjectName("lbEyeNum")
        self.lbMouthNum = QtWidgets.QLabel(self.centralwidget)
        self.lbMouthNum.setGeometry(QtCore.QRect(560, 100, 67, 21))
        self.lbMouthNum.setObjectName("lbMouthNum")
        self.spinSize = QtWidgets.QSpinBox(self.centralwidget)
        self.spinSize.setGeometry(QtCore.QRect(220, 150, 48, 21))
        self.spinSize.setMinimum(50)
        self.spinSize.setMaximum(1000)
        self.spinSize.setSingleStep(10)
        self.spinSize.setProperty("value", 450)
        self.spinSize.setObjectName("spinSize")
        self.lbSize = QtWidgets.QLabel(self.centralwidget)
        self.lbSize.setGeometry(QtCore.QRect(270, 150, 81, 21))
        self.lbSize.setObjectName("lbSize")
        self.lbStatus = QtWidgets.QLabel(self.centralwidget)
        self.lbStatus.setGeometry(QtCore.QRect(16, 190, 271, 41))
        self.lbStatus.setObjectName("lbStatus")
        self.frame = QtWidgets.QLabel(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 280, 581, 400))
        self.frame.setObjectName("frame")
        self.lbInfoEye = QtWidgets.QLabel(self.centralwidget)
        self.lbInfoEye.setGeometry(QtCore.QRect(10, 240, 151, 31))
        self.lbInfoEye.setObjectName("lbInfoEye")
        self.lbInfoMouth = QtWidgets.QLabel(self.centralwidget)
        self.lbInfoMouth.setGeometry(QtCore.QRect(180, 240, 151, 31))
        self.lbInfoMouth.setObjectName("lbInfoMouth")
        self.lbWarn = QtWidgets.QLabel(self.centralwidget)
        self.lbWarn.setGeometry(QtCore.QRect(360, 240, 151, 31))
        self.lbWarn.setObjectName("lbWarn")
        self.checkDropbox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkDropbox.setGeometry(QtCore.QRect(20, 120, 171, 21))
        self.checkDropbox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.checkDropbox.setObjectName("checkDropbox")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 617, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "blink"))
        self.btnStart.setText(_translate("MainWindow", "Start"))
        self.lbEyeThread.setText(_translate("MainWindow", "Eyes Threadhold"))
        self.lbMouthThread.setText(_translate("MainWindow", "Mouth Threadhold"))
        self.lbEyeFrame.setText(_translate("MainWindow", "Eyes Frame"))
        self.lbMouthFrame.setText(_translate("MainWindow", "Mouth Frame"))
        self.lbCam.setText(_translate("MainWindow", "Camera Source"))
        self.checkShow.setText(_translate("MainWindow", "Show Frames"))
        self.lbEyeNum.setText(_translate("MainWindow", "TextLabel"))
        self.lbMouthNum.setText(_translate("MainWindow", "TextLabel"))
        self.lbSize.setText(_translate("MainWindow", "Frame Size"))
        self.lbStatus.setText(_translate("MainWindow", "TextLabel"))
        self.frame.setText(_translate("MainWindow", "TextLabel"))
        self.lbInfoEye.setText(_translate("MainWindow", "TextLabel"))
        self.lbInfoMouth.setText(_translate("MainWindow", "TextLabel"))
        self.lbWarn.setText(_translate("MainWindow", "TextLabel"))
        self.checkDropbox.setText(_translate("MainWindow", "Dropbox"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())