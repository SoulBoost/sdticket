"""
класс Outlook

класс, который формирует и отправляет сообщение в sd от имени пользователя
сообщение отправляется с помощью библиотеки win32com.client

конструктор класса принимает:
    user: объект класса User,
    problem_name: str,
    comment='',
    image='' путь к изображению

объекты класса:
        self.user: объект класса User
        self.to = SD_EMAIL: str почта sd
        self.problem_name: str
        self.comment: str
        self.body = self.set_body() - str тело сообщение формируется по шаблону
        self.subject = 'Для администраторов_#' + self.problem_name - str
        self.image: str путь к изображению
"""

import os
import win32com.client as win32

from Classes.User import User
from Global.globals import SD_EMAIL
from Classes.Ip import Ip


class Outlook:
    def __init__(self, user: User, problem_name: str, comment='', image=''):
        self.user = user
        self.to = SD_EMAIL
        self.problem_name = problem_name
        self.comment = comment
        self.body = self.set_body()
        self.subject = 'Для администраторов_#' + self.problem_name
        self.image = image

# комментарий к заявке куда писать?
    def set_body(self):
        body = f'Локация: {self.user.get_dealership()}\n\n' \
               f'( Login: {self.user.get_login()},\n\n' \
               f'{self.user.get_pc_name()}' \
               f'\n\n{self.comment}' \
               f'\n\n Пилот'
        return body

    def send_message(self):
        outlook = win32.Dispatch('outlook.application')
        mail = outlook.CreateItem(0)
        mail.To = self.to
        mail.Subject = self.subject
        mail.Body = self.body
        mail.Importance = 2
        # mail.HTMLBody = '<h2>HTML Message body</h2>' #this field is optional

        if self.image:
            attachment = os.path.join(os.getcwd(), self.image)
            print(attachment)
            try:
                mail.Attachments.Add(attachment)
            except Exception as e:
                print(e)

        try:
            mail.Send()
            return 'Сообщение отправлено'
        except Exception as e:
            return e

    def get_to(self):
        return self.to

    def get_subject(self):
        return self.subject

    def get_body(self):
        return self.body


if __name__ == '__main__':
    ip = Ip()
    user = User.new(ip)
    outlook = Outlook(user, 'fdfbfd', 'ghjytjyr')
    print(outlook.get_to(), outlook.get_subject(), outlook.get_body())
    outlook.send_message()
