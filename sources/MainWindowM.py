"""
класс MainWindow

класс, который реализует логику интерфейса


конструктор класса принимает:
    user: объект класса User

объекты класса:
    self.combo_location - список ДЦ, оно выбирается автоматически по имени ПК
    self.combo_theme - список проблем. подтягиваются через json, работа с ними идет через экземпляры класса Ticket
    self.button_send - кнопка отправки сообщения (или запуска bat файла)
                       доступна только когда все необходимые поля заполнены
    self.text_comment - пользователь описывает проблему
    self.label_comment - подсказка что писать пользователю
    self.text_comment2 - пользователь описывает проблему
    self.label_comment2 - подсказка что писать пользователю
    self.label_ip
    self.label_pc_name
"""

from PyQt5.QtWidgets import QApplication, QMessageBox, QSystemTrayIcon, QMenu, QAction
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import Qt

from Global.globals import THEMES, PATH_B_BAT, PATH_B, PATH_TEMP_CLEAN, PATH_CACHE_CLEANING
from MainWindowV import MainWindowV
from Classes.Ip import Ip
# from Classes.Outlook import Outlook
from Classes.User import User
from Global.run_bat import run_bat, run_bat_out, path_existance


class MainWindow(MainWindowV):
    def __init__(self, user: User):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.view()

        self.user = user
        self.all_locations = []
        self.set_all_locations()
        self.set_current_combo_location()

        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(QtGui.QIcon('Pictures/SD.ico'))
        self.tray_icon.setToolTip('SD Ticket')

        show_action = QAction("Отправить заявку", self)
        hide_action = QAction("Спрятать", self)
        show_action.triggered.connect(self.over_show)
        hide_action.triggered.connect(self.hide)
        tray_menu = QMenu()
        tray_menu.addAction(show_action)
        tray_menu.addAction(hide_action)
        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.show()

        self.check_manyally_location.setChecked(True)
        self.label_ip.setText('IP: ' + self.user.get_ip())
        self.label_pc_name.setText('Имя компьютера: ' + self.user.get_pc_name())
        self.label_worktime.setText('Время работы ПК: часы, минуты')
        self.tray_icon.activated.connect(self.on_tray_activated)
        self.button_send.clicked.connect(self.button_route)
        self.check_manyally_location.toggled.connect(self.enable_location)
        self.combo_theme.currentTextChanged.connect(self.combo_changed)
        self.comboBox.currentTextChanged.connect(self.comboBox_changed)
        self.text_comment.textChanged.connect(self.text_changed)
        self.text_comment2.textChanged.connect(self.text_changed)

    # активировать кнопку если есть комментарий
    def text_changed(self):
        if (len(self.text_comment2.toPlainText()) >= THEMES[self.combo_theme.currentText()].get_comment_len2() and
                len(self.text_comment.toPlainText()) >= THEMES[self.combo_theme.currentText()].get_comment_len()):
            self.button_send.setDisabled(False)
        else:
            self.button_send.setDisabled(True)

    # замена оборудования
    def comboBox_changed(self):
        if self.comboBox.currentText() == "Прочее":
            self.enable_text(THEMES[self.combo_theme.currentText()].get_help_info())
            self.button_send.setDisabled(True)
        else:
            self.hide_text()
            self.label_comment.setText(THEMES[self.combo_theme.currentText()].get_help_info())
            self.button_send.setDisabled(False)

    # активировать кнопку или комментарий в зависимости от выбранной проблемы
    def combo_changed(self):
        problem = self.combo_theme.currentText()
        if THEMES[problem].get_ticket_type() == 4:
            self.hide_comboBox()
            self.enable_text(THEMES[problem].get_help_info())
            self.enable_text2(THEMES[problem].get_help_info2())
        elif THEMES[problem].get_ticket_type() == 3:
            self.hide_text()
            self.hide_text2()
            self.hide_comboBox()
            self.button_send.setDisabled(False)
        elif THEMES[problem].get_ticket_type() == 2:
            self.hide_comboBox()
            self.hide_text2()
            self.enable_text(THEMES[problem].get_help_info())
        elif THEMES[problem].get_ticket_type() == 1:
            self.hide_text()
            self.hide_text2()
            self.enable_comboBox(THEMES[problem].get_subselection(), THEMES[problem].get_help_info())
        elif THEMES[problem].get_ticket_type() == 0:
            self.hide_text()
            self.hide_text2()
            self.hide_comboBox()
            self.button_send.setDisabled(False)

    # скрывает поле комбо бокс
    def hide_comboBox(self):
        self.comboBox.setMaximumSize(QtCore.QSize(1, 1))
        self.comboBox.clear()
        self.label_comment.setText('')
        self.comboBox.setDisabled(True)

    # показывает поле комбо бокс
    def enable_comboBox(self, objects: list, text='Комментарий'):
        self.comboBox.setMaximumSize(QtCore.QSize(1000000, 40))
        self.comboBox.clear()
        self.comboBox.addItems(objects)
        self.label_comment.setText(text)
        self.comboBox.setDisabled(False)
        self.comboBox_changed()

    # скрывает поле комментарий и лейбл-подсказку
    def hide_text(self):
        self.text_comment.setMaximumSize(QtCore.QSize(1, 1))
        self.text_comment.setText('')
        self.label_comment.setText('')
        self.text_comment.setDisabled(True)

    # показывает поле комментарий и лейбл-подсказку
    def enable_text(self, text="Комментарий"):
        self.text_comment.setMaximumSize(QtCore.QSize(1000000, 40))
        self.label_comment.setText(text)
        self.text_comment.setDisabled(False)
        self.text_comment.setText('')
        self.text_changed()

    # скрывает поле комментарий и лейбл-подсказку
    def hide_text2(self):
        self.text_comment2.setMaximumSize(QtCore.QSize(1, 1))
        self.text_comment2.setText('')
        self.label_comment2.setText('')
        self.text_comment2.setDisabled(True)

    # показывает поле комментарий и лейбл-подсказку
    def enable_text2(self, text="Комментарий"):
        self.text_comment2.setMaximumSize(QtCore.QSize(1000000, 40))
        self.label_comment2.setText(text)
        self.text_comment2.setDisabled(False)
        self.text_comment2.setText('')

    # по клику на галочку активировать выбор ДЦ
    def enable_location(self):
        if self.check_manyally_location.isChecked():
            self.set_current_combo_location()
            self.combo_location.setDisabled(True)
        else:
            if self.create_question_box("SD ticket", "Если вы измените локацию, ваш запрос отправится администраторам,"
                                                     "выбранной вами локации.\n"
                                                     "Вы уверены, что хотите изменить локацию?"):
                self.check_manyally_location.setChecked(True)
                return 'connected'
            self.combo_location.setDisabled(False)

    # содержит список всех дц
    def set_all_locations(self):
        for i in range(self.combo_location.count()):
            self.all_locations.append(self.combo_location.itemText(i))

    def set_user_dealership(self):
        self.user.set_dealership(self.combo_location.currentText())

    # автоматически выбрать ДЦ
    def set_current_combo_location(self):
        self.user.set_auto_dealership()

        if self.user.get_dealership() in self.all_locations:
            self.combo_location.setCurrentText(self.user.get_dealership())

    # если тип проблемы 3 (запустить bat) и поле комментарий заполнено, то отправить заявку
    def button_route(self):
        if THEMES[self.combo_theme.currentText()].get_ticket_type() == 3 and \
                self.text_comment.toPlainText() == "":
            try:
                method = getattr(self, THEMES[self.combo_theme.currentText()].get_related_method())
                method()
            except Exception as e:
                print(e)
        else:
            self.send()

    # почисть кэш
    def clean_temp(self):
        error_code = run_bat(PATH_TEMP_CLEAN)
        print(error_code)
        error_code = run_bat(PATH_CACHE_CLEANING)
        print(error_code)
        if self.create_question_box("SD ticket", "Временные файлы удалены.\n"
                                                 "Я могу помочь вам чем-нибудь ещё?"):
            self.hide()

    # подключить диск B
    def connect_B(self):
        if path_existance(PATH_B):
            if self.create_question_box("SD ticket", "Доступ к диску B уже предоставлен.\n"
                                                     "Вы хотите отправить заявку в SD?"):
                return 'connected'

            self.enable_text("Пожалуйста опишите свою проблему более детально")
            return 'sending'

        error_code = run_bat(PATH_B_BAT)
        if not error_code and path_existance(PATH_B):
            if self.create_question_box("SD ticket", "Доступ к диску B предоставлен.\n"
                                                     "Я могу помочь вам чем-нибудь ещё?"):
                self.hide()
            return 'connected'

        answer = run_bat_out(PATH_B_BAT)
        self.text_comment.setText(answer[1])
        self.send()
        self.text_comment.setText('')
        return 'sent'

    # наследовать новый класс от QMessageBox и убрать у него крестик
    def create_question_box(self, title: str, text: str):
        msg = QMessageBox()
        msg.setWindowIcon(QtGui.QIcon('Pictures/SD.ico'))
        msg.ckicked_no = True
        msg.setText(text)
        msg.setWindowTitle(title)
        msg_no = msg.addButton("Нет", msg.NoRole)
        msg_yes = msg.addButton("Да", msg.YesRole)

        def clicked_msg_yes():
            msg.ckicked_no = False

        msg_yes.clicked.connect(clicked_msg_yes)
        msg.exec_()
        return msg.ckicked_no

    # отправить сообщение локальным адиминам
    def send(self):
        # do_screen('Pictures/error_screen.png')
        self.set_user_dealership()
        comment = ''
        # в будущем исправить
        if THEMES[self.combo_theme.currentText()].get_ticket_type() == 3:
            comment += 'Сообщение об ошибке: '
        else:
            comment += 'Комментарий пользователя: '

        # комментарий - это либо текст бокс, либо комбо бокс
        if self.text_comment.toPlainText():
            comment += self.text_comment.toPlainText()
        elif self.comboBox.currentText():
            comment += self.comboBox.currentText()

        if self.text_comment2.toPlainText():
            comment += '\n'
            comment += self.text_comment2.toPlainText()

        outlook = Outlook(self.user, self.combo_theme.currentText(), comment)
        answer = outlook.send_message()
        print(answer)

        if self.create_question_box("SD ticket", "Заявка направлена вашим локальным администраторам\n"
                                                 "Я могу помочь вам чем-нибудь ещё?"):
            self.hide()

    def keyPressEvent(self, event):
        # print(event.key())
        if event.key() == Qt.Key_Space:
            event.key()
        if event.key() == Qt.Key_B:
            event.key()

    def on_tray_activated(self, reason):
        if reason == self.tray_icon.DoubleClick:
            self.over_show()

    def closeEvent(self, event):
        event.ignore()
        self.hide()

    def over_show(self):
        if self.windowState() == QtCore.Qt.WindowMinimized:
            self.setWindowState(QtCore.Qt.WindowNoState)
        self.show()


if __name__ == "__main__":
    ip = Ip()
    user = User.new(ip)
    app = QApplication([])
    ui = MainWindow(user)
    ui.show()
    app.exec()
