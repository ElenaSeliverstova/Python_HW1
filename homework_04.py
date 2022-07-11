# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

quater_number = int(input('Введите номер четверти '))
if 4 < quater_number > 0:
    print('mistake')
elif quater_number == 1:
    print('диапазон x > 0 и y > 0')
elif quater_number == 2:
    print('диапазон x < 0  и y > 0')
elif quater_number == 3:
    print('диапазон x < 0 и y < 0')
else:
    print('диапазон x > 0 и y < 0')
