"""
класс Ip

класс, который содержит информацию о компьютере пользователя
вытягивает данные используя библиотеку socket

    self.ip: str типа 'xxx.xxx.xxx.xxx'
    self.pc_name: str типа "DESCTOP-xxxxx"
    self.dealership: str определяется по имени компьютера
    self.subnet: str определяется по IP. Сейчас не используется. Определяет по IP подсеть пользователя. Зачем?
"""

import socket
import time
import uptime

from Global.globals import SUBNETS, PC_NAMES


class Ip:
    def __init__(self):
        self.ip = socket.gethostbyname(socket.getfqdn())
        self.pc_name = socket.gethostname()
        self.dealership = self.set_dealership_by_pc_name()
        self.worktime = self.get_worktime()
#  время работы ПК
    def get_worktime(self):
        n = int(uptime.uptime())
        if (n // 3600 ) > 24:
            return "Необходимо перезагрузить устройство\nКомпьютер работает более 24 часов."
        return

# по префиксу в имени ПК определяет ДЦ с помощью PC_names.json
    def set_dealership_by_pc_name(self):
        for prefix in PC_NAMES.keys():
            if prefix in self.pc_name:
                return PC_NAMES[prefix]
        return "не определено"

# возвращает ip как десятичное число
    def ip_to_bit(self, ipv4):
        a, b, c, d = map(int, ipv4.split('.'))
        bin_ip = (a << 24) + (b << 16) + (c << 8) + d
        return bin_ip

# получает подсеть в виде xxx.xxx.xxx.xxx/xx
# возвращает маску как десятичное число
    def get_bin_mask(self, subnet):
        length = int(subnet.split('/')[1])  # префикс подсети
        mask = int('1' * length + '0' * (32-length), 2)
        return mask



# опереляет ДЦ по подсети с помощью Subnets.json
    def set_dealership(self):
        if not self.subnet:
            return None
        dealership = SUBNETS[self.subnet]
        if dealership[0] == '*' or dealership == 'не определена':
            return None
        return dealership

    def get_ip(self):
        return self.ip

    def get_subnet(self):
        return self.subnet

    def get_dealership(self):
        return self.dealership

    def get_pc_name(self):
        return self.pc_name


if __name__ == '__main__':
    user_ip = Ip()
    # print()
    # print(user_ip.get_dealership(), user_ip.get_subnet(), user_ip.get_ip(), user_ip.get_pc_name(), user_ip.get_worktime())
