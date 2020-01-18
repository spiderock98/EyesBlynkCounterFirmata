# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets, QtSerialPort
from scipy.spatial import distance as dist
from imutils.video import VideoStream,FPS
from imutils import face_utils
from threading import Thread
import numpy as np
import playsound
import argparse
import imutils
import time
import dlib
import cv2
from pyfirmata import ArduinoNano, util
import glob
import serial
import cameraindex


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(605, 286)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboPort = QtWidgets.QComboBox(self.centralwidget)
        self.comboPort.setGeometry(QtCore.QRect(150, 20, 91, 25))
        self.comboPort.setObjectName("comboPort")
        self.lbPort = QtWidgets.QLabel(self.centralwidget)
        self.lbPort.setGeometry(QtCore.QRect(100, 20, 31, 21))
        self.lbPort.setObjectName("lbPort")
        self.btnStart = QtWidgets.QPushButton(self.centralwidget)
        self.btnStart.setGeometry(QtCore.QRect(370, 150, 111, 25))
        self.btnStart.setObjectName("btnStart")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(10, 190, 591, 41))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.spinEye = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.spinEye.setGeometry(QtCore.QRect(150, 55, 69, 31))
        self.spinEye.setAccelerated(False)
        self.spinEye.setMaximum(0.5)
        self.spinEye.setSingleStep(0.01)
        self.spinEye.setProperty("value", 0.24)
        self.spinEye.setObjectName("spinEye")
        self.lbEyeThread = QtWidgets.QLabel(self.centralwidget)
        self.lbEyeThread.setGeometry(QtCore.QRect(20, 60, 121, 21))
        self.lbEyeThread.setObjectName("lbEyeThread")
        self.lbMouthThread = QtWidgets.QLabel(self.centralwidget)
        self.lbMouthThread.setGeometry(QtCore.QRect(10, 100, 131, 31))
        self.lbMouthThread.setObjectName("lbMouthThread")
        self.spinMouth = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.spinMouth.setGeometry(QtCore.QRect(150, 100, 69, 31))
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
        self.lbEyeFrame.setGeometry(QtCore.QRect(290, 60, 81, 17))
        self.lbEyeFrame.setObjectName("lbEyeFrame")
        self.lbMouthFrame = QtWidgets.QLabel(self.centralwidget)
        self.lbMouthFrame.setGeometry(QtCore.QRect(280, 100, 91, 21))
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
        self.lbCam.setGeometry(QtCore.QRect(270, 20, 111, 20))
        self.lbCam.setObjectName("lbCam")
        self.checkShow = QtWidgets.QCheckBox(self.centralwidget)
        self.checkShow.setGeometry(QtCore.QRect(90, 150, 111, 21))
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
        self.spinSize.setProperty("value", settings.value('spinSize'))
        self.spinSize.setSingleStep(10)
        self.spinSize.setObjectName("spinSize")
        self.lbSize = QtWidgets.QLabel(self.centralwidget)
        self.lbSize.setGeometry(QtCore.QRect(270, 150, 81, 21))
        self.lbSize.setObjectName("lbSize")
        self.lbStatus = QtWidgets.QLabel(self.centralwidget)
        self.lbStatus.setGeometry(QtCore.QRect(16, 190, 271, 41))
        self.lbStatus.setObjectName("lbStatus")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 605, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        ########### init ###########
        self.spinSize.setEnabled(False)
        self.lbSize.setEnabled(False)
        self.lbEyeNum.setText('0')
        self.lbMouthNum.setText('0')

        ########### custom ###########
        ports = QtSerialPort.QSerialPortInfo.availablePorts()
        for i,port in enumerate(ports):
            self.comboPort.insertItem(i, port.portName())

        self.comboSource.addItems([str(cameraindex.index('HD'))])

        self.slideEye.valueChanged.connect(self.slideChange)
        self.slideMouth.valueChanged.connect(self.slideChange)
        
        self.progressBar.setTextVisible(True)

        self.btnStart.clicked.connect(self.onClick)

        self.checkShow.stateChanged.connect(self.showChange)

    def showChange(self):
        if (self.checkShow.isChecked()):
            self.spinSize.setEnabled(True)
            self.lbSize.setEnabled(True)
        else:
            self.spinSize.setEnabled(False)
            self.lbSize.setEnabled(False)

    def slideChange(self):
        eyeVal = self.slideEye.value()
        mouthVal = self.slideMouth.value()

        self.lbEyeNum.setText(str(eyeVal))
        self.lbMouthNum.setText(str(mouthVal))
        settings.setValue('lbEyeNum', eyeVal)
        settings.setValue('lbMouthNum', mouthVal)
    
    def onClick(self):
        def progressValue(stt, current, total=10):
            self.lbStatus.setText(stt)
            self.progressBar.setValue((current/total)*100)

        def sound_alarm():
            playsound.playsound('alarm.wav')

        def sound_confirm():
            playsound.playsound('confirm.mp3')

        def eye_aspect_ratio(eye):
            A = dist.euclidean(eye[1], eye[5])
            B = dist.euclidean(eye[2], eye[4])
            C = dist.euclidean(eye[0], eye[3])
            return (A + B) / (2.0 * C)

        def mouth_ratio(mouth):
            AB = dist.euclidean(mouth[12],mouth[16])
            CD = dist.euclidean(mouth[13],mouth[19])
            EF = dist.euclidean(mouth[14],mouth[18])
            GH = dist.euclidean(mouth[15],mouth[17])
            return (CD+EF+GH)/(3.0*AB)

        progressValue('Initial Constant Values', 1)
        
        ledRED = 2
        ledYELLOW = 3
        ledGREEN = 4

        # EYE_THRESH = self.spinEye.value()
        # MOUTH_THRESH = self.spinMouth.value()
        # EYE_CONTINOUS_FRAMES = self.slideEye.value()
        # MOUTH_CONTINOUS_FRAMES = self.slideMouth.value()

        COUNTER_EYES = COUNTER_MOUTH = COUNTER_COMMAND = 0
        ALARM_ON = CONFIRM_ON = False

        progressValue('Loading face detector', 2)
        # print("[INFO] loading facial landmark predictor...")
        detector = dlib.get_frontal_face_detector()
        progressValue('Loading facial landmark predictor', 3)
        predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

        progressValue('Loading facial coordinates', 5)
        (lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
        (rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]
        (mouthStart, mouthEnd) = face_utils.FACIAL_LANDMARKS_IDXS["mouth"]

        progressValue('Opening serial port', 6)
        # print("[INFO] opening serial port...")
        # board = ArduinoNano('COM11')
        board = ArduinoNano('/dev/' + self.comboPort.currentText())

        progressValue('Starting video stream thread', 7)
        # print("[INFO] starting video stream thread...")
        vs = VideoStream(src=0).start()
        progressValue('FPS sclaler', 8)
        fps = FPS().start()
        progressValue('Sleep in 1 second', 9)
        time.sleep(1.0)
        progressValue('Done', 10)

        while True:
            frame = vs.read()
            frame = imutils.resize(frame, self.spinSize.value())
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            rects = detector(gray, 0)

            for rect in rects:
                shape = predictor(gray, rect)
                shape = face_utils.shape_to_np(shape)

                leftEye = shape[lStart:lEnd]
                rightEye = shape[rStart:rEnd]
                mouth = shape[mouthStart:mouthEnd]

                avr_eyes = (eye_aspect_ratio(leftEye) + eye_aspect_ratio(rightEye)) / 2.0
                avr_mouth = mouth_ratio(mouth)

                for item in (leftEye):
                    cv2.circle(frame, tuple(item), 2, (0,255,0),-1)
                for item in (rightEye):
                    cv2.circle(frame, tuple(item), 2, (0,255,0),-1)
                for item in (mouth):
                    cv2.circle(frame, tuple(item), 2, (0,255,0),-1)

                # if avr_eyes < EYE_THRESH:
                if avr_eyes < self.spinEye.value():
                    COUNTER_EYES += 1

                    # if COUNTER_EYES >= EYE_CONTINOUS_FRAMES:
                    if COUNTER_EYES >= self.slideEye.value():
                        
                        if not ALARM_ON:
                            ALARM_ON = True
                            COUNTER_COMMAND += 1
                            t = Thread(target=sound_alarm)
                            t.deamon = True
                            t.start()
                        # cv2.putText(frame, "DROWSINESS ALERT!", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                else:
                    # open eyes to reset these values
                    COUNTER_EYES = 0
                    ALARM_ON = False

                # if avr_mouth > MOUTH_THRESH:
                if avr_mouth > self.spinMouth.value():
                    COUNTER_MOUTH += 1

                    # if COUNTER_MOUTH >= MOUTH_CONTINOUS_FRAMES:
                    if COUNTER_MOUTH >= self.slideMouth.value():
                        if not CONFIRM_ON:
                            CONFIRM_ON = True
                            
                            # arduino
                            if COUNTER_COMMAND == 1:
                                board.digital[ledRED].write(1)
                            elif COUNTER_COMMAND == 2:
                                board.digital[ledYELLOW].write(1)
                            elif COUNTER_COMMAND == 3:
                                board.digital[ledGREEN].write(1)

                            COUNTER_COMMAND = 0

                            t = Thread(target=sound_confirm)
                            t.deamon = True
                            t.start()
                        cv2.putText(frame, "CONFIRM COMMAND!", (frame.shape[0]-30, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                else:
                    # open eyes to reset these values
                    COUNTER_MOUTH = 0
                    CONFIRM_ON = False

                cv2.putText(frame, "Average Eyes: {:.2f}".format(avr_eyes), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                cv2.putText(frame, "Average Mouth: {:.2f}".format(avr_mouth), (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                cv2.putText(frame, "Command: {}".format(COUNTER_COMMAND), (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 100, 255), 2)

            if(self.checkShow.isChecked()):
                cv2.imshow("Frame", frame)

            if cv2.waitKey(1) == 27:
                break

            fps.update()

        fps.stop()
        print("FPS trung binh: {:.2f}".format(fps.fps()))
        cv2.destroyAllWindows()
        vs.stop()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "blink"))
        self.lbPort.setText(_translate("MainWindow", "Port"))
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
        


if __name__ == "__main__":
    import sys
    settings = QtCore.QSettings('setting.ini', QtCore.QSettings.IniFormat)
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
