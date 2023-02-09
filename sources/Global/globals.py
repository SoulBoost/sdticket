"""
Глобальные переменные
"""

import os
from dotenv import load_dotenv

from Classes.Ticket import Ticket
from Global.read_json import json_to_dict
from find_path import path_to_env

print('a=', path_to_env)

# ../ чтобы запустить из какой-то папки
cdir = os.getcwd()
prefix = ''
if cdir.split('\\')[-2] == 'AdminHelper':
    prefix = r'..\\'

# выгружаем переменные окружения
dotenv_path = os.path.join(os.path.dirname(__file__), '..\\Resources\\.env')

# вроде пофиксил. 2 раза, чтобы наверняка
is_found = load_dotenv(cdir + '\\Resources\\.env')
if not is_found:
    is_found = load_dotenv(path_to_env)
print(is_found)

DOMAIN = os.getenv('DOMAIN')
SD_EMAIL = os.getenv('SD_EMAIL')
print(SD_EMAIL)
ROLF_DNS_SUFFIX = os.getenv('ROLF_DNS_SUFFIX')

PATH_TEMP_CLEAN = os.getenv('PATH_TEMP_CLEAN')
PATH_CACHE_CLEANING = os.getenv('PATH_CACHE_CLEANING')
PATH_B_BAT = os.getenv('PATH_B_BAT')
PATH_B = os.getenv('PATH_B')

SUBNETS = json_to_dict(prefix + "Resources/Subnets.json", encoding="utf-8-sig")
PRINT_SERVERS = json_to_dict(prefix + "Resources/Print_servers.json")
PRINTERS_ROOMS = json_to_dict(prefix + "Resources/Printers_rooms.json")
PC_NAMES = json_to_dict(prefix + "Resources/PC_names.json", encoding="utf-8-sig")

# 0 - просто отправить
# 1 - выбрать из списка
# 2 - написать руками
# 3 - запустить bat
# 4 - два текст бокса. первый - написать имя принтера, второй - описать проблему.
THEMES = {}
tickets = json_to_dict(prefix + "Resources/TicketTemplates.json")

for key in tickets.keys():
    ticket = Ticket(key, ticket_type=tickets[key]['ticket_type'],
                    help_info=tickets[key]['help_info'],
                    subselection=tickets[key]['subselection'],
                    comment_len=tickets[key]['comment_len'],
                    related_method=tickets[key]['related_method'],
                    help_info2=tickets[key]['help_info2'],
                    comment_len2=tickets[key]['comment_len2'])
    THEMES[ticket.get_name()] = ticket


DSS = []
for pc in PC_NAMES.keys():
    if PC_NAMES[pc] not in DSS:
        DSS.append(PC_NAMES[pc])


if __name__ == '__main__':
    for key in THEMES.keys():
        print(THEMES[key].get_name(), THEMES[key].get_ticket_type(), THEMES[key].get_help_info(),
              THEMES[key].get_subselection(), THEMES[key].get_comment_len(), THEMES[key].get_related_method())
