from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtCore import Qt

from Global.globals import THEMES, DSS
from View.MainWindow import Ui_MainWindow


class MainWindowV(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindowV, self).__init__()
        self.setupUi(self)
        self.view()

    def view(self):
        self.setWindowIcon(QtGui.QIcon('Pictures/SD.ico'))

        self.combo_location.addItems(DSS)
        # self.combo_theme.addItems(THEMES.keys())

        for key in THEMES.keys():
            self.combo_theme.addItem(THEMES[key].get_name())

        self.text_comment.setMaximumSize(1, 1)
        self.comboBox.setMaximumSize(1, 1)
        self.text_comment2.setMaximumSize(1, 1)

        # self.text_comment.setPlaceholderText("Пожалуйста опишите свою проблему более детально")
        self.combo_location.setDisabled(True)
        self.button_send.setDisabled(True)
        self.text_comment.setDisabled(True)


if __name__ == "__main__":
    app = QApplication([])

    # Force the style to be the same on all OSs:
    app.setStyle("Fusion")

    # Now use a palette to switch to dark colors:
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(53, 53, 53))
    palette.setColor(QPalette.WindowText, Qt.white)
    palette.setColor(QPalette.Base, QColor(25, 25, 25))
    palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
    palette.setColor(QPalette.ToolTipBase, Qt.black)
    palette.setColor(QPalette.ToolTipText, Qt.white)
    palette.setColor(QPalette.Text, Qt.white)
    palette.setColor(QPalette.Button, QColor(53, 53, 53))
    palette.setColor(QPalette.ButtonText, Qt.white)
    palette.setColor(QPalette.BrightText, Qt.red)
    palette.setColor(QPalette.Link, QColor(42, 130, 218))
    palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
    palette.setColor(QPalette.HighlightedText, Qt.black)
    app.setPalette(palette)

    ui = MainWindowV()
    ui.show()
    app.exec()
