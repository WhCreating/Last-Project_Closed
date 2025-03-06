from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QGridLayout, QWidget, QMessageBox, QMainWindow, QApplication, QDialog
from PyQt5.QtCore import QCoreApplication, QSettings, QUrl, QThread, pyqtSignal
from info_micro import list_microphones
from os import path
from window1 import Ui_MainWindow
from info_micro import list_microphones
from win_main2 import Window2
from time import sleep
import webbrowser
import toml
import asyncio
import llama
import asyncio
from skillvaShell import *
from multiprocessing import Process



press_btn = False
class Window(QMainWindow, QThread):
    update_signal = pyqtSignal(str)
    def __init__(self):
        super().__init__()
        
        #Наследование
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        #проверка
        parent_dir = path.dirname(path.abspath(__file__))
        with open(path.join(parent_dir, 'settings', 'config.ini'), 'r') as f:
            global confss
            confss = toml.load(f)
            confss['zapusk'] = 'False'
            if confss['theme'] == 0:
                self.setStyleSheet("background-color: \'#121212\';\n""\n""")
                self.ui.label_4.setStyleSheet("color: \'white\';\n""background: none;")
            else :
                self.setStyleSheet("background-color: \'white\';\n""\n""")
                self.ui.title_text_2.setStyleSheet("color: \'black\';\n""background: none;")
                self.ui.label_4.setStyleSheet("color: \'black\';\n""background: none;")


        #Импорт иконок:
        #TitleWin


        icon = QtGui.QIcon()
        parent_dir = path.dirname(path.abspath(__file__))
        icon.addPixmap(QtGui.QPixmap(path.join(parent_dir,"texture","icontit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        
        #Кнопка запуска ассистента


        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(path.join(parent_dir,"texture","icontit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ui.btn_play.setIcon(icon1)
        self.ui.btn_play.setFlat(True)
        self.ui.btn_play.clicked.connect(self.start_ass)
        
        #Кнопка настроек
        
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(path.join(parent_dir,"texture","icon_settings.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ui.btn_settings.setIcon(icon2)
        self.ui.btn_settings.setFlat(True)
        
        #buttons_settings
        
        self.ui.btn_settings.clicked.connect(self.new_window_event)
        
        self.wn2 = Window2(self)

        # label_4
        self.ui.label_4.setGeometry(QtCore.QRect(20, 130, 351, 90))
        
        #Галвный текст

        
        #Обработка ответа на promt
        #global promt
        #promt = asyncio.run(llama.chat('Привет'))
        
        
    def open_url(self):
        webbrowser.open_new('http:/vaskill.rf.gd')
        
    def new_window_event(self): 
        self.wn2.show()
        #self.hide()
        
    def start_ass(self):
        parent_dir = path.dirname(path.abspath(__file__))
        global press_btn
        if press_btn == False:
            icon_play = QtGui.QIcon()
            icon_play.addPixmap(QtGui.QPixmap(path.join(parent_dir, 'texture', 'icontit.png')))
            self.ui.btn_play.setIcon(icon_play)
            press_btn = True
            confss['zapusk'] = 'True'

            self.ui.label_4.setText("Выполняется. . .")

            text = shell(micros=confss['micro'], mod=confss['mod_use'])
            self.ui.label_4.setText(text)


            press_btn = False


            #self.ui.label_4.setText(promt)
        elif press_btn == True:
            icon_play1 = QtGui.QIcon()
            icon_play1.addPixmap(QtGui.QPixmap(path.join(parent_dir, 'texture', 'icontit.png')))
            self.ui.btn_play.setIcon(icon_play1)
            press_btn = False
            confss['zapusk'] = 'False'
            print(press_btn)
            return 0
            
        




        
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())