# -*- coding: utf-8 -*-
"""
Задание 7.1

Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком
виде на стандартный поток вывода:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
atr = ['Prefix', 'AD/Metric', 'Next-Hop', 'Last update', 'Outbound Interface']

with open('ospf.txt') as f:
    for line in f:
        line = (((line.replace('via', ' ')).replace(',', ' '))).split()
        line = line[1:]
        j = 0
        for i in atr:
            if j == 1:
                line[j] = line[j].strip('[]')
                print('{:22}{}'.format(i, line[j]))
                j += 1
            else:
                print('{:22}{}'.format(i, line[j]))
                j += 1

