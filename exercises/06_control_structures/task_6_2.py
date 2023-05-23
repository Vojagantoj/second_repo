# -*- coding: utf-8 -*-
"""
Задание 6.2

Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
В зависимости от типа адреса (описаны ниже), вывести на стандартный поток вывода:
   'unicast' - если первый байт в диапазоне 1-223
   'multicast' - если первый байт в диапазоне 224-239
   'local broadcast' - если IP-адрес равен 255.255.255.255
   'unassigned' - если IP-адрес равен 0.0.0.0
   'unused' - во всех остальных случаях

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
p = input ('Введите адрес в формате X.X.X.X: ')
ip = p.split('.')
i = 0
ips = []
while i < 4:
    k = int(ip[i])
    ips.append(int(ip[i]))
    i += 1
if 1 <= ips[0] <= 223:
    print('unicast')
elif 224 <= ips[0] <= 239:
    print('multicast')
elif ips[0] == ips[1] == ips[2] == ips[3] == 255:
    print('local broadcast')
elif ips[0] == ips[1] == ips[2] == ips[3] == 0:
    print('unassigned')
else:
    print('unused')