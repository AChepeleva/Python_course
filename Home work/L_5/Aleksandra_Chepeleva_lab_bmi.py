# # Home work L5
# # BMI

# def get_data():
#     """Функция для ввода корректных данных."""
#     while True:
#         try:
#             weight = float(input("Введите вес в килограммах:"))
#             break
#         except ValueError:
#             print("Ошибка! Введите числовое значение.")
    
#     while True:
#         try:
#             height = int(input("Введите рост в сантиметрах:"))
#             break
#         except ValueError:
#                 print("Ошибка! Введите числовое значение.")
#     return weight, height


# def bmi(weight, height):
#     """Функция, которая рассчитывает индекс массы тела."""
#     if height < 100 or height > 250 or \
#     weight < 20 or weight > 200:
#         return None
    
#     return weight / (height/100) ** 2


# def analyze_bmi(weight, height):
#     """Функция для анализа полученного BMI"""
#     bmi_value = bmi(weight, height)
    
#     if bmi_value is None:
#         return "Неверные данные"

#     if bmi_value < 18.5:
#         return "Дефицит массы тела!"
#     elif 18.5 <= bmi_value <= 25:
#         if 150 <= height <= 200 and 45 <= weight <=99:
#             return "Норма массы тела!"
#         return "Дефицит массы тела!"
#     elif 25 < bmi_value < 30:
#         return "Предожирение!"
#     elif 30 <= bmi_value < 35:
#         return "Ожирение 1-ой степени!"
#     elif 35 <= bmi_value < 40:
#         return "Ожирение 2-ой степени!"
#     else:
#         return "Ожирение 3-ей степени!"
    

# def main():
#     weight, height = get_data()

#     print(f"Вес: {weight} кг, Рост: {height} см")
#     print("BMI: ", bmi(weight, height))
#     print("Анализ: ", analyze_bmi(weight, height))

# main()
