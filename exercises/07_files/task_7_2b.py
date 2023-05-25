# -*- coding: utf-8 -*-
"""
Задание 7.2b

Переделать скрипт из задания 7.2a: вместо вывода на стандартный поток вывода,
скрипт должен записать полученные строки в файл

Имена файлов нужно передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore
и строки, которые начинаются на '!'.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
from sys import argv

namefirst = argv[1]
namelast = argv[2]

ignore = ["duplex", "alias", "configuration"]
result = []
with open(namefirst) as f:
    for line in f:
        g = False
        for ig in ignore:
            if ig in line:
                g = True
                break
        if line.startswith('!'):
            pass
        elif line.startswith(' ') and g == False:
            result.append(line)
        elif g == False:
            result.append(line)
results = ''.join(result)
d = open(namelast, 'w')
d.write(results)
d.close()