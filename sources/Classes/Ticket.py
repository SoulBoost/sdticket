# coding=cp1251

"""
����� Ticket

�����, ������� �������� ���������� � ���� ������ (��������), ��� � ��� ������
� ����� ���������� ����� ��������� ������������

    self.name - �������� ��������
    self.ticket_type - ��� �������� 0-4. �� ���� ������� ����� ���������� ����� ��������� ������������
    self.help_info - ����� ��������� ��� ������� ������������
    self.subselection - ������ ����� � �������� ����� ������ �� ������ ��������
    self.comment_len - ����������� ����� ����������� ������������
    self.related_method - ��� ������, ������� ����� ��������� �� ������� ������
    self.help_info2 - ������ ����� ���������

0 - ������ ���������
1 - ������� �� ������
2 - �������� ������
3 - ��������� bat
4 - ��� ����� �����. ������ - �������� ��� ��������, ������ - ������� ��������.
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
    print(test_themes['������/�������� ������������'])

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
