
import example_2 as file

print(file.f(1))

colors = ['red', 'green', 'blue']
data = open('file.txt', 'a')
# a – открытие для добавления данных, добавление данных
# r – открытие для чтения данных
# w – открытие для записи данных, перезапись данных
data.writelines(colors) # запись в одну строку
data.write('\nline 1\n') # запись с новой строки
data.close()

with open('file.txt', 'w') as data:
    data.write('line 1\n')
    data.write('line 2\n')
# с конструкцией with не нужно писать data.close() для закрытия файла

path = 'file.txt'
data = open(path, 'r')
for line in data:
    print(line)
data.close()
