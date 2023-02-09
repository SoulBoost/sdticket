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

from Classes.Ip import Ip


class User:
    __object = None

    @staticmethod
    def new(ip):
        if User.__object == None:
            User.__object = User(ip)
        return User.__object

    def __init__(self, ip: Ip):
        self.ip_cl = ip
        self.pc_name = ip.get_pc_name()
        self.login = os.environ.get("USERNAME")
        self.ip = ip.get_ip()
        self.dealership = ip.get_dealership()
        # self.worktime = get_worktime()

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

    def get_worktime(self):
        return self.worktime


if __name__ == '__main__':
    ip = Ip()
    user = User.new(ip)
    user.set_dealership('Центр')
    print(user.get_pc_name(), user.get_login(), user.get_ip(), user.get_dealership())
    print(user)

    ip.ip = '10.50.7.169'
    ip.subnet = ip.set_subnet()
    ip.dealership = ip.set_dealership()
    user2 = User.new(ip)
    print(user2.get_pc_name(), user2.get_login(), user2.get_ip(), user2.get_dealership())
    print(user2)
