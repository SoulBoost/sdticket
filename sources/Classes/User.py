"""
класс User

Singleton класс, который одержит информацию о пользователе

конструктор класса принимает:
    ip: объект класса Ip,

объекты класса:
        self.pc_name: str берется из ip
        self.login: str берется через библиотеку os
        self.ip: str берется из ip
        self.dealership: str берется из ip
"""

import os
import uptime
import socket

# from Classes.Ip import Ip
from Global.globals import SUBNETS, PC_NAMES


class User:
    __object = None

    @staticmethod
    def new(ip):
        if User.__object is None:
            User.__object = User(ip)
        return User.__object

    def __init__(self, ip):
        self.pc_name = socket.gethostname()
        self.ip_cl = ip
        self.login = os.environ.get("USERNAME")
        self.ip = ip.get_ip()

        self.worktime = self.get_worktime()

        self.dealership = self.set_dealership_by_pc_name()
        self.ip = socket.gethostbyname(socket.getfqdn())

    def set_auto_dealership(self):
        self.dealership = self.ip_cl.get_dealership()

    def set_pc_name(self, pc_name):
        self.pc_name = pc_name

    def set_login(self, login):
        self.login = login

    def set_ip(self, ip):
        self.ip = ip

    def set_dealership(self, dealership):
        self.dealership = dealership

    def get_dealership(self):
        return self.dealership

    def get_pc_name(self):
        return self.pc_name

    def get_login(self):
        return self.login

    def get_ip(self):
        return self.ip

    # время работы ПК
    def get_worktime(self):
        n = int(uptime.uptime())
        if (n // 3600) > 24:
            return "Необходимо перезагрузить устройство\nКомпьютер работает более 24 часов."
        return

    # название ПК
    def get_pc_name(self):
        return self.pc_name

    # по префиксу в имени ПК определяет ДЦ с помощью PC_names.json
    def set_dealership_by_pc_name(self):
        for prefix in PC_NAMES.keys():
            if prefix in self.pc_name:
                return PC_NAMES[prefix]
            return "не определено"


if __name__ == '__main__':
    ip = User
    # user_ip = User() #
    user = User.new(ip)
