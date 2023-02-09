from PyQt5.QtWidgets import QApplication

from Classes.Ip import Ip
from Classes.User import User
from MainWindowM import MainWindow


# pyinstaller -F -w -i "C:\Users\ivodo\PycharmProjects\AdminHelper\Pictures\SD.ico" SD_Ticket.py
def app():
    ip = Ip()
    user = User.new(ip)
    app = QApplication([])
    ui = MainWindow(user)
    app.exec()


if __name__ == '__main__':
    app()
