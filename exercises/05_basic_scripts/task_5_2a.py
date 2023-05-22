# -*- coding: utf-8 -*-
"""
Задание 5.2a

Всё, как в задании 5.2, но, если пользователь ввел адрес хоста, а не адрес сети,
надо преобразовать адрес хоста в адрес сети и вывести адрес сети и маску,
как в задании 5.2.

Пример адреса сети (все биты хостовой части равны нулю):
* 10.0.1.0/24
* 190.1.0.0/16

Пример адреса хоста:
* 10.0.1.1/24 - хост из сети 10.0.1.0/24
* 10.0.5.195/28 - хост из сети 10.0.5.192/28

Если пользователь ввел адрес 10.0.1.1/24, вывод должен быть таким:

Network:
10        0         1         0
00001010  00000000  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000


Проверить работу скрипта на разных комбинациях хост/маска, например:
    10.0.5.195/28, 10.0.1.1/24

Вывод сети и маски должен быть упорядочен также, как в примере:
- столбцами
- ширина столбца 10 символов (в двоичном формате
  надо добавить два пробела между столбцами
  для разделения октетов между собой)


Подсказка:
Есть адрес хоста в двоичном формате и маска сети 28. Адрес сети это первые 28 бит
адреса хоста + 4 ноля.
То есть, например, адрес хоста 10.1.1.195/28 в двоичном формате будет
bin_ip = "00001010000000010000000111000011"

А адрес сети будет первых 28 символов из bin_ip + 0000 (4 потому что всего
в адресе может быть 32 бита, а 32 - 28 = 4)
00001010000000010000000111000000

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
ipm = input('Введите адрес устройства в формате X.X.X.X/XX: ')
ip = ((ipm.split('/'))[0]).split('.')
m = int((ipm.split('/'))[1])
mask = "1" * m + "0" * (32 - m)
p = "{:08b}".format(int(ip[0])) + "{:08b}".format(int(ip[1])) + "{0:08b}".format(int(ip[2])) + "{0:08b}".format(int(ip[3]))
newp = p[:m] + "0" * (32 - m)
newip = [int(newp[0:8], 2), int(newp[8:16], 2), int(newp[16:24], 2), int(newp[24:], 2)]

ip_template = '''
Network:
{0:<8}  {1:<8}  {2:<8}  {3:<8}
{0:08b}  {1:08b}  {2:08b}  {3:08b}

Mask:
/{4}
{5:<8}  {6:<8}  {7:<8}  {8:<8}
{5:08b}  {6:08b}  {7:08b}  {8:08b}
'''
d = [m, int(mask[0:8], 2), int(mask[8:16], 2), int(mask[16:24], 2), int(mask[24:], 2),]
print(ip_template.format(int(newip[0]), int(newip[1]), int(newip[2]), int(newip[3]), int(d[0]), int(d[1]), int(d[2]), int(d[3]), int(d[4])))