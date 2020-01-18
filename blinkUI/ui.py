# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets, QtSerialPort
from scipy.spatial import distance as dist
from imutils.video import VideoStream, FPS
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(447, 254)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(50, 70, 86, 25))
        self.comboBox.setObjectName("comboBox")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 70, 67, 17))
        self.label.setObjectName("label")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(160, 10, 256, 192))
        self.listWidget.setObjectName("listWidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 120, 89, 25))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 447, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.ports = QtSerialPort.QSerialPortInfo.availablePorts()
        for i,port in enumerate(self.ports):
            self.comboBox.insertItem(i,port.portName())
        # self.comboBox.addItems(['Nano','Uno','Mega'])

        self.pushButton.clicked.connect(self.onClick)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "blink"))
        self.label.setText(_translate("MainWindow", "Port"))
        self.pushButton.setText(_translate("MainWindow", "Click"))
    def onClick(self):
        def serial_ports():
            for port in glob.glob('/dev/tty[A-Za-z]*'):
                try:
                    s = serial.Serial(port)
                    s.close()
                    return port
                except (OSError, serial.SerialException):
                    pass
            print('Connecting Error ...')

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
         
        ledRED = 2
        ledYELLOW = 3
        ledGREEN = 4

        EYE_THRESH = 0.24
        MOUTH_THRESH = 0.27
        EYE_CONTINOUS_FRAMES = 15
        MOUTH_CONTINOUS_FRAMES = 15

        COUNTER_EYES = COUNTER_MOUTH = COUNTER_COMMAND = 0
        ALARM_ON = CONFIRM_ON = False

        print("[INFO] loading facial landmark predictor...")
        detector = dlib.get_frontal_face_detector()
        predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

        (lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
        (rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]
        (mouthStart, mouthEnd) = face_utils.FACIAL_LANDMARKS_IDXS["mouth"]

        print("[INFO] opening serial port...")
        # board = ArduinoNano('COM11')
        board = ArduinoNano('/dev/'+self.comboBox.currentText())

        print("[INFO] starting video stream thread...")
        vs = VideoStream(src=2).start()
        fps = FPS().start()
        time.sleep(1.0)

        while True:
            frame = vs.read()
            frame = imutils.resize(frame, width=900)
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

                if avr_eyes < EYE_THRESH:
                    COUNTER_EYES += 1

                    if COUNTER_EYES >= EYE_CONTINOUS_FRAMES:
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

                if avr_mouth > MOUTH_THRESH:
                    COUNTER_MOUTH += 1

                    if COUNTER_MOUTH >= MOUTH_CONTINOUS_FRAMES:
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

            fps.update()

            cv2.imshow("Frame", frame)

            if cv2.waitKey(1) == 27:
                break

        fps.stop()
        print("FPS trung binh: {:.2f}".format(fps.fps()))
        cv2.destroyAllWindows()
        vs.stop()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication([])
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
