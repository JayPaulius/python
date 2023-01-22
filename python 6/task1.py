# Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,*. приоритет операций стандартный.
# *Пример:*
# 2+2 => 4;
# 1+2*3 => 7;
# 1-2*3 => -5;
# - Добавьте возможность использования скобок, меняющих приоритет операций.
# *Пример:*
# 1+2*3 => 7;
# (1+2)*3 => 9;

def split_expression(text):
    list1 = []
    value = ''
    for i in range(len(text)):
        if text[i].isdigit() and i != len(text)-1 or text[i] == '.' or text[i] == '-' and text[i+1].isdigit() and text[i-1] == '(' or i == 0:
            value += text[i]
        elif text[i].isdigit() and i == len(text)-1:
            value += text[i]
            list1.append(value)
        else:
            if value != '':
                list1.append(value)
            list1.append(text[i])
            value = ''
    return list1

def brackets(list1, index):
    list2 = []
    for i in range(index+1, len(list1)):
        if list1[i] == ')':
            break
        list2.append(list1[i])
    while len(list2) > 1:
        for i in range(len(list2)):
            if '*' in list2  or '/' in list2:
                if list2[i] == '*':
                    list2[i-1] = float(list2[i-1]) * float(list2[i+1])
                    list2[i] = ''
                    list2[i+1] = ''
                    break
                elif list2[i] == '/':
                    list2[i-1] = float(list2[i-1]) / float(list2[i+1])
                    list2[i] = ''
                    list2[i+1] = ''
                    break
            else:
                if list2[i] == '+':
                    list2[i-1] = float(list2[i-1]) + float(list2[i+1])
                    list2[i] = ''
                    list2[i+1] = ''
                    break
                elif list2[i] == '-':
                    list2[i-1] = float(list2[i-1]) - float(list2[i+1])
                    list2[i] = ''
                    list2[i+1] = ''
                    break
        list2 = list(filter(None, list2))
    return list2[0]

def calculate_expression(text):
    list1 = split_expression(text)
    while len(list1) > 1:
        for i in range(len(list1)):
            if '(' in list1:
                if list1[i] == '(' and '(' not in list1[i+1:]:
                    list1[i] = brackets(list1, i)
                    i += 1
                    while True:
                        if list1[i] != ')':
                            list1[i] = ''
                            i += 1
                        else:
                            list1[i] = ''
                            break
                    break
            elif '*' in list1  or '/' in list1:
                if list1[i] == '*':
                    list1[i-1] = float(list1[i-1]) * float(list1[i+1])
                    list1[i] = ''
                    list1[i+1] = ''
                    break
                elif list1[i] == '/':
                    list1[i-1] = float(list1[i-1]) / float(list1[i+1])
                    list1[i] = ''
                    list1[i+1] = ''
                    break
            else:
                if list1[i] == '+':
                    list1[i-1] = float(list1[i-1]) + float(list1[i+1])
                    list1[i] = ''
                    list1[i+1] = ''
                    break
                elif list1[i] == '-':
                    list1[i-1] = float(list1[i-1]) - float(list1[i+1])
                    list1[i] = ''
                    list1[i+1] = ''
                    break
        if list1[0] != 0:
            list1 = list(filter(None, list1))
        else:
            list1 = list1[:1]
    list1[0] = round(float(list1[0]), 3)
    return list1

def main():
    text = input('Введите выражение без пробелов: ')
    list1 = calculate_expression(text)
    print(list1)

main()