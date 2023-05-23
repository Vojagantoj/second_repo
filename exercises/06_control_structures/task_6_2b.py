# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова.

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'
Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
p = input ('Введите адрес в формате X.X.X.X: ')
Tr = False
while not Tr:
    i = 0
    ips = []
    ip = p.split('.')
    while i < 4 and ip[i].isdigit() and int(ip[i]) in range(256)  and p.count('.') == 3 and len(p.split('.')) == 4:
        ips.append(int(ip[i]))
        i += 1
        if i == 4:
            pass
        elif i < 4:
            continue
        if 1 <= ips[0] <= 223:
            print('unicast')
            Tr = True
            break
        elif 224 <= ips[0] <= 239:
            print('multicast')
            Tr = True
            break
        elif ips[0] == ips[1] == ips[2] == ips[3] == 255:
            print('local broadcast')
            Tr = True
            break
        elif ips[0] == ips[1] == ips[2] == ips[3] == 0:
            print('unassigned')
            Tr = True
            break
        else:
            print('unused')
            Tr = True
            break
    else:
        print('Неправильный IP-адрес')
        p = input('Введите новый адрес: ')