
from functools import reduce

numbers = [2, 3, 4, 5]

result = reduce(lambda x, y: x*y, numbers)
print("Умножение всех чисел в списке:", result)