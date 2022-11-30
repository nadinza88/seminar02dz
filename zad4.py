# Задайте числами список из N элементов, заполненных из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

import random
n = int(input('Введите число: '))
sp = []
for i in range(1, (n+1)):
    sp.append(random.randrange((-n), (n+1)))

for i in range(len(sp)):
    sp[i] = str(sp[i] * sp[i])

data = open('file.txt', 'w') 
for line in sp:
    data.writelines(line + '\n')
 
data.close
exit()