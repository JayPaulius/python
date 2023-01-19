# В файле находится N натуральных чисел, записанных через пробел. 
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. 
# Найдите это число.


with open('file.txt', 'r') as data:
    string = data.read().split()
list1 = list(map(int, string))
for i, el in enumerate(list1[:-1]):
    if el != list1[i+1] - 1:
        print(list1[i] + 1)

# n = [1,2,3,4,5,6,8,9]
# print(*[val for i, val in enumerate(n[1:]) if val != n[i] + 1])

# for i in range(1, len(list1)):
#     if list1[i-1] != list1[i] - 1:
#         print(list1[i])
#         break