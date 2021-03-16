import os
dir = 'some_data'
n = 1
some_dict = {}
for n in range(1, 6):
    some_dict[10 ** n] = len([file for file in os.scandir(dir) if 10 ** (n-1) < os.stat(file.path).st_size <= 10 ** n])
s_d = sorted(some_dict)
for k in s_d:
    print(k, ':', some_dict[k])


