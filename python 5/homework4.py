# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

def read_file(path):
    with open(path, 'r') as data:
        text1 = data.read()
    return text1

def write_file(path, text2):
    with open(path, 'w') as data:
        data.write(text2)

def encoding(text1):
    print(text1)
    list1 = list(text1)
    count = 0
    text2 = ''
    char = list1[0]
    for e in list1:
        if e == char:
            count += 1
        else:
            text2 += str(count) + char
            char = e
            count = 1
    text2 += str(count) + char
    print(text2)
    return text2

def decoding(text1):
    print(text1)
    text2 = ''
    value = ''
    for e in text1:
        if e.isdigit():
            value += e
        else:
            for i in range(int(value)):
                text2 += e
            value = ''
    print(text2)
    return text2

def main():
    mode = int(input('Выберите режим работы: кодирование - 1, декодирование - 2: '))
    while mode > 2 or mode < 1:
        mode = int(input('Выберите режим работы: кодирование - 1, декодирование - 2: '))
    if mode == 1:
        text1 = read_file('file1.txt')
        text2 = encoding(text1)
        write_file('file2.txt', text2)
    else:
        text1 = read_file('file2.txt')
        text2 = decoding(text1)
        write_file('file1.txt', text2)
main()