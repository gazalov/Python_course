# 1.3[6]. Вы пользуетесь общественным транспортом? 
# Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, 
# де сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета.

# 	Примеры/Тесты:
# 	385916 >>> yes
# 	123456 >>> no

# ```(*)``` **Усложнение.** Вывод результат на экран сделайте одной строкой(только один print), 
# для этого используйте тернарный оператор

bilet = int(input('Введите номер билета: '))
bilet_left = bilet // 1000
bilet_right = bilet % 1000

def sum_digits(bilet_half):
    sum_bilet = 0
    while bilet_half > 0:
        sum_bilet = sum_bilet + bilet_half % 10
        bilet_half = bilet_half // 10
    return sum_bilet

if sum_digits(bilet_left) == sum_digits(bilet_right):
    print('yes')
else:
    print('no')

#усложнение
print('yes') if sum_digits(bilet_left) == sum_digits(bilet_right) else print('no')
