from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QGridLayout, QWidget, QMessageBox, QMainWindow, QApplication, QDialog
from PyQt5.QtCore import QCoreApplication, QSettings
from info_micro import list_microphones
from os import path
from window2 import Ui_MainWindow
from info_micro import list_microphones
import toml
from pathlib import Path
from mods import *

class Window2(QMainWindow, QDialog):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        #Наследование
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global parent_dir
        parent_dir = path.dirname(path.abspath(__file__))

        # imports mods
        all_imported_modules = import_all_modules()

        #проверки
        
        parent_dir = path.dirname(path.abspath(__file__))
        #Работает, не трогать!!!
        with open(path.join(parent_dir, 'settings', 'config.ini'), 'r') as f:
            confss = toml.load(f)

        #Загрузка настроек
        
        with open(path.join(parent_dir, 'settings', 'config.ini'), 'r') as f:
            confs = toml.load(f)

        global config
        config = confs
        
        
        #Импорт иконок:
        #TitleIcon
        
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(path.join(parent_dir, "texture","icontit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        
        #Значения
        
        _translate = QtCore.QCoreApplication.translate
        self.ui.lineEdit_5.setText(_translate("MainWindow", path.join(parent_dir, 'models', 'small_model_ru')))
        
        #TitleText5
        
        #self.ui.title_text_5.setText('Модель распознавания речи')
        #radioButton
        if config['or_radio'] == 0:
            self.ui.radioButton.setChecked(True)
            self.ui.radioButton_2.setChecked(False)
        else:
            self.ui.radioButton.setChecked(False)
            self.ui.radioButton_2.setChecked(True)

        name_mode = all_imported_modules[config["mod_use"]].name()
        self.ui.radioButton_2.setText(name_mode)

        #pushButton
        
        self.ui.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        
        #pushButton_2
        
        self.ui.pushButton_3.clicked.connect(self.dial)
        
        #textline_3
        
        self.ui.lineEdit_3.setText(config['name_bot'])

        #mods

        all_mod = import_all_modules()

        if all_mod[config['mod_use']].types() == 'voice':
            self.ui.radioButton_2.setText(all_mod[config['mod_use']].name())

        #listWidget

        p = Path(".\\mods")
        for x in p.rglob("*.py"):
            x1 = str(x).replace('.py', '').replace('mods\\', '')
            if x1 == '__init__':
                continue
            else :
                self.ui.listWidget.addItem(str(x1))

        self.ui.listWidget.currentItem()
        #-----------------------------
        info_mic = list_microphones()
        
        self.ui.comboBox.addItem(f'Нет')
        for i, mics in enumerate(info_mic):
                mi = mics.split()
                if mi[0] == 'Microphone':
                        self.ui.comboBox.addItem(f'{i}:{mics}')
                else :
                        mi[0] = 'Микрофон'
                        mi.pop(1)
                        self.ui.comboBox.addItem(f'{i}:{str(mics)}')
        #TabWidget
        self.ui.tabWidget.setCurrentIndex(0)
        #comboBox
        self.ui.comboBox.currentIndexChanged.connect(self.change_micro)
        self.ui.comboBox.setCurrentIndex(config['micro'])
        #comboBox2
        self.ui.comboBox_2.currentIndexChanged.connect(self.change_theme)
        self.ui.comboBox_2.setCurrentIndex(config['theme'])
        #pushbutton
        self.ui.pushButton.clicked.connect(self.clicks_used)
        self.ui.lineEdit_5.setText(config['model'])
        #line_edit 
        #event window

    def izmenit(self):
        config['or_radio'] = 0

    def izmenit1(slef):
        config['or_radio'] = 1

    def change_micro(self, value):
        config['micro'] = value
        
    def change_theme(self, value):
        config['theme'] = value
        
    def clicks_used(self):
        config['name_bot'] = self.ui.lineEdit_3.text()
        if self.ui.listWidget.selectedItems():
            currInd = self.ui.listWidget.currentRow()
            item = self.ui.listWidget.item(currInd)
            config['mod_use'] = item.text()
            if self.ui.radioButton.isChecked() == True:
                config['or_radio'] = 0
            elif self.ui.radioButton_2.isChecked() == True:
                config['or_radio'] = 1
            else:
                print("Распознователь не выбран")

            print(config)
            with open(path.join(parent_dir, 'settings', 'config.ini'), 'w') as f:
                confs = toml.dump(config, f)
        else:
            if self.ui.radioButton.isChecked() == True:
                config['or_radio'] = 0
            elif self.ui.radioButton_2.isChecked() == True:
                config['or_radio'] = 1
            else:
                print("Распознователь не выбран")

            print(config)
            with open(path.join(parent_dir, 'settings', 'config.ini'), 'w') as f:
                confs = toml.dump(config, f)
        
        
#Выбор категории
    def action_click(self):
        self.dial()  
    
    
    def dial(self):
            
        fname = QFileDialog.getExistingDirectory(self, "Выберите путь до модели")
        self.ui.lineEdit_5.setText(str(fname))
        config['model'] = self.ui.lineEdit_5.text()
        if fname == '':
                
                mess_box = QMessageBox()
                mess_box.setWindowTitle('Ошибка')
                mess_box.setText('Выберите модель!')
                mess_box.setIcon(QMessageBox.Information)
                mess_box.setStandardButtons(QMessageBox.Ok)
                mess_box.buttonClicked.connect(self.action_click)
                
                mess_box.exec_()
                
                
                
            
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = Window2()
    window.show()
    sys.exit(app.exec_())