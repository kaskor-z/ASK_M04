from fake_math import divide as fake_divide
from true_math import divide as true_divide

result1 = fake_divide(69, 3)
result2 = fake_divide(3, 0)
result3 = true_divide(49, 7)
result4 = true_divide(15, 0)
print('\nРезультат деления № 1 = ', result1)
print('Результат деления № 2 = ', result2)
print('Результат деления № 3 = ', result3)
print('Результат деления № 4 = ', result4)

#       Для удобства анализа - дополнительный код cо вводом
#       приизвольный комбинаций пар исходных чисел

f_ = int(input('\nВведите значения числителя = '))
s_ = int(input('Введите значения знаменателя = '))
result1 = fake_divide(f_, s_)
result2 = true_divide(f_, s_)
print('Результат деления № 1 (не дозволено делить на 0) = \t', result1)
print('Результат деления № 2 (дозволено делить на 0) = \t', result2)
