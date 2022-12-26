# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

def read_file(path):
    with open(path, 'r') as data:
        for line in data:
            string = line.rstrip()
    return string

def get_polynom_nums(polynom):
    string = ''
    for i in range(len(polynom)):
        if polynom[i].isdigit() == True and polynom[i-1] != '^' and polynom[i-2] != '=':
            string += polynom[i]
            if polynom[i+1].isdigit() == False:
                string += ' '
    list1 = list(map(int, string.split()))
    return list1

def get_polynom_degree(polynom):
    index = polynom.find('^') + 1
    degree = int(polynom[index])
    return degree

def sum(polynom1, polynom2):
    polynom3 = ''
    index = 0
    degree = get_polynom_degree(polynom1)
    polynom1_nums = get_polynom_nums(polynom1)
    polynom2_nums = get_polynom_nums(polynom2)
    for i in range(degree, -1, -1):
        if i > 0:
            polynom3 += f'{polynom1_nums[index] + polynom2_nums[index]} * x^{i} + '
        else:
            polynom3 += f'{polynom1_nums[index] + polynom2_nums[index]} = 0'
        index += 1
    return polynom3

def main():
    polynom1 = read_file('file1.txt')
    polynom2 = read_file('file2.txt')
    print(polynom1)
    print(polynom2)
    print(f'сумма многочленов: {sum(polynom1, polynom2)}')

main()