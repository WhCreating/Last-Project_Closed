from voicer import recording
import config
import config_main
from synthesis import synthes
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QFrame
import sys
#from llama import chat
from win_main1 import Window
from win_main2 import Window2

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())