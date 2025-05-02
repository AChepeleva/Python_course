# # Home work 5.1
# # Написать функцию, которая принимает на вход значение (год) и определяет високосный год (True) 
# # или нет (False).

# def is_year_leap(year):
#    '''Функция проверяет является ли год високосным.
#     Високосный год: 
#     1. Делится на 4 без остатка, но не делится нацело на 100.
#     2. Делится на 4 без остатка, делится на 100 без остатка, делится на 400 без остатка.'''
   
#    if year % 4 != 0:
#        return False
#    elif year % 100 != 0:
#        return True
#    elif year % 400 != 0:
#        return False
#    return True


# test_data = [1500, 1900, 2000, 2016, 1987]
# test_result = [False, False, True, True, False]

# for year, result in zip(test_data, test_result): # zip() - параллельный перебор двух последовательностей
#     if is_year_leap(year) == result:
#         print(year, 'is leap? -->', result)
#     else:
#         print(year, 'from your func -->', \
#               is_year_leap(year))
#         print('but expected -->', result)
