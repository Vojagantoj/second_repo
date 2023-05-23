# -*- coding: utf-8 -*-
"""
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса.
Адрес считается корректно заданным, если он:
   - состоит из 4 чисел (а не букв или других символов)
   - числа разделенны точкой
   - каждое число в диапазоне от 0 до 255

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'

Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
p = input ('Введите адрес в формате X.X.X.X: ')
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
        break
    elif 224 <= ips[0] <= 239:
        print('multicast')
        break
    elif ips[0] == ips[1] == ips[2] == ips[3] == 255:
        print('local broadcast')
        break
    elif ips[0] == ips[1] == ips[2] == ips[3] == 0:
        print('unassigned')
        break
    else:
        print('unused')
        break
else:
    print('Неправильный IP-адрес')