# 6.2[32]: Определить индексы элементов массива (списка), значения которых принадлежат заданному 
# диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

# 	Напишите функцию
#     - Аргументы: список чисел и границы диапазона
#     - Возвращает: список индексов элементов (смотри условие)

# 	Примеры/Тесты:
#     lst1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
#     <function_name>(lst1, 2, 10) -> [1, 3, 7, 9, 10, 13, 14, 19]
#     <function_name>(lst1, 2, 9) -> [1, 3, 7, 10, 13, 19]
#     <function_name>(lst1, 0, 6) -> [2, 3, 6, 7, 10, 11, 16]

# ```(*)``` **Усложнение.**  Для формирования списка внутри функции используйте Comprehension

# ```(*)``` **Усложнение.**  Функция возвращает список кортежей вида: индекс, значение

# 	Примеры/Тесты:
#     lst1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
#     <function_name>(lst1, 2, 10) -> [(1, 9), (3, 3), (7, 4), (9, 10), (10, 2), (13, 8), (14, 10), (19, 7)]

lst1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]

def index_in_range(lst, el_min, el_max):
    lst_rez = []
    for idx in range(len(lst)):
        if  el_min <= lst[idx] <= el_max:
            lst_rez.append(idx)
    return lst_rez

#усложнение
def index_in_range_comp(lst, el_min, el_max):
    lst_rez = [num for num in range(0, len(lst)) if el_min <= lst[num] <= el_max]
    return lst_rez

#усложнение
def index_in_range_tuple(lst, el_min, el_max):
    lst_rez = [(num, lst[num]) for num in range(0, len(lst)) if el_min <= lst[num] <= el_max]
    return lst_rez

print(index_in_range(lst1, 2, 10))
print(index_in_range_comp(lst1, 2, 10))
print(index_in_range_tuple(lst1, 2, 10))