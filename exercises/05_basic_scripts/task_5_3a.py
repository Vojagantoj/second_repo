# -*- coding: utf-8 -*-
"""
Задание 5.3a

Дополнить скрипт из задания 5.3 таким образом, чтобы, в зависимости
от выбранного режима, задавались разные вопросы в запросе о номере
VLANа или списка VLANов:
* для access: 'Введите номер VLAN:'
* для trunk: 'Введите разрешенные VLANы:'

Ограничение: Все задания надо выполнять используя только пройденные темы.
То есть эту задачу можно решить без использования условия if и циклов for/while.
"""

mode = input('Введите режим работы интерфейса (access/trunk): ')
int = input('Введите тип и номер интерфейса: ')
vlans = dict(access = 'Введите номер VLAN: ', trunk = 'Введите разрешенные VLANы: ')
vlan = input(vlans.get(mode))

templates = dict(
trunk = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan {}",
]
,
access = [
    "switchport mode access",
    "switchport access vlan {}",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
])

print('interface {}'.format(int))
print('\n'.join(templates.get(mode)).format(vlan))