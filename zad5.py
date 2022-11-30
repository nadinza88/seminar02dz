# Реализуйте алгоритм перемешивания списка (shuffle использовать нельзя, другие методы из библиотеки random - можно).

import random 
n = [1, 2, 3, 4]
n = random.sample(n, len(n))
print(n)