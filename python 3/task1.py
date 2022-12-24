#  Реализуйте алгоритм задания случайных чисел без использования встроенного генератора псевдослучайных чисел.

import time
seconds = time.time()
print((seconds))
print(int(seconds * 100 % 100))

# from datetime import datetime
# import time
# def random():
#     local_time = str(datetime.now())
#     ms = list(map(int, list(local_time[-6:])))
#     for i in ms:
#         if i == 0:
#             ms.remove(0)
#     prod = 1
#     for i in range(len(ms)):
#         prod *= int(ms[i])
#     if i == len(ms)-1:
#         for _ in range(4):
#             prod *= prod
#     ms2 = (str(prod)[5:6])
    
#     if ms2 == '':
#         while ms2 == '':
#             local_time = str(datetime.now())
#             ms = list(map(int, list(local_time[-6:])))
#             for i in ms:
#                 if i == 0:
#                     ms.remove(0)
#             prod = 1
#             for i in range(len(ms)):
#                 prod *= int(ms[i])
#             if i == len(ms)-1:
#                 for _ in range(4):
#                     prod *= prod
#             ms2 = (str(prod)[5:6])

#     return int((ms2))

# for i in range(50):
#     print(random(), end=' ')
#     time.sleep(0.01)
