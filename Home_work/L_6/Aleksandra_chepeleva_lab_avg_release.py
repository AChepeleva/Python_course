# # Home work L3

# def avg(score):
#     """ Функция для вычисления среднего бала студента.
#     Arguments:
#     score - tuple - набор оценок.
#     Returns:
#     float - средний бал, 2 знака послсе запятой.
#     """
#     return round((sum(score)/len(score)),2)


# def new_grade(student_name, grade):
#     """Функция для добавления новой оценки студенту.
#     Arguments:
#     student_name - str - имя, не менее 2-х символов.
#     grade - int - оценка.
#     Returns:
#     True - если оценка добавлен ауспешно.
#     False - если имя меньше 2 символов.
#     """
#     if len(student_name) < 2:
#         return False
    
#     student_name = student_name.title()

#     if student_name in student_grades:
#         student_grades.update({student_name: student_grades.get(student_name) + (grade,)})
#     else:
#         student_grades.update({student_name:(grade, )})

#     return True

# def show_grades():
#     print("show_grades")

#     if not student_grades:
#         print("Нет оценок студентов.")
#     else:
#         for key, value in student_grades.items():
#             print("name:", key)
#             print("grades:", value)

        
# def show_avg():
#     print("show avg")
#     for key, value in student_grades.items():
#         print("name:", key)
#         print("avg:", avg(value))


# def main():
#     msg = """1 - new grade
#     2 - show avg
#     3 - show grades
#     quit - exit from programm
#     """
#     oper = input(msg)

#     while oper != "quit":
#         match oper:
#             case "1":
#                 name = input("Put full name:")
#                 grade = int(input("Put grade:"))
#                 new_grade(name, grade)
#             case "2":
#                 show_avg()
#             case "3":
#                 show_grades()
#             case _:
#                 print("Sorry, ne ponial")
#         oper = input(msg)

# student_grades= {}
# main()
