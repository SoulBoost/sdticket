# coding=cp1251

"""
класс Ticket

класс, который содержит информацию о типе заявки (проблемы), что с ней делать
и какую информацию нужно заполнить пользователю

    self.name - название проблемы
    self.ticket_type - тип проблемы 0-4. от типа зависит какую информацию нужно заполнить пользователю
    self.help_info - лэйбл подсказка что вводить пользователю
    self.subselection - список вещей с которыми можем помочь по данной проблеме
    self.comment_len - минимальная длина комментария пользователя
    self.related_method - имя метода, который нужно запустить по нажатии кнопки
    self.help_info2 - вторая лэйбл подсказка

0 - просто отправить
1 - выбрать из списка
2 - написать руками
3 - запустить bat
4 - два текст бокса. первый - написать имя принтера, второй - описать проблему.
"""

from Global.read_json import json_to_dict


class Ticket:
    def __init__(self, name: str, ticket_type=0, help_info='', subselection=None,
                 comment_len=0, related_method='send', help_info2='', comment_len2=0):
        if subselection is None:
            subselection = ['']
        self.name = name
        self.ticket_type = ticket_type
        self.help_info = help_info
        self.subselection = subselection
        self.comment_len = comment_len
        self.related_method = related_method
        self.help_info2 = help_info2
        self.comment_len2 = comment_len2

    def get_name(self):
        return self.name

    def get_ticket_type(self):
        return self.ticket_type

    def get_help_info(self):
        return self.help_info

    def get_subselection(self):
        return self.subselection

    def get_comment_len(self):
        return self.comment_len

    def get_related_method(self):
        return self.related_method

    def get_help_info2(self):
        return self.help_info2

    def get_comment_len2(self):
        return self.comment_len2


if __name__ == '__main__':
    tickets = []

    test_themes = json_to_dict("../Resources/TicketTemplates.json")
    print(test_themes)
    print(test_themes['Выдать/заменить оборудование'])

    for key in test_themes.keys():
        ticket = Ticket(key, ticket_type=test_themes[key]['ticket_type'],
                        help_info=test_themes[key]['help_info'],
                        subselection=test_themes[key]['subselection'],
                        comment_len=test_themes[key]['comment_len'],
                        related_method=test_themes[key]['related_method'])
        tickets.append(ticket)
    for ticket in tickets:
        print(ticket)
        print(ticket.get_name(), ticket.get_ticket_type(), ticket.get_help_info(),
              ticket.get_subselection(), ticket.get_comment_len(), ticket.get_related_method())
