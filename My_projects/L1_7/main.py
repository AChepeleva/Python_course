from Package_geometry_calc.Shapes.triangle import tr_perimeter, tr_area
from Package_geometry_calc.Shapes.square import sq_perimeter, sq_area
from Package_geometry_calc.Shapes.rectangle import rec_perimeter, rec_area
from Package_geometry_calc.Shapes.circle import cir_perimeter, cir_area
from Package_geometry_calc.History_journal.journal import add_to_journal, get_my_journal
from input_data import input_triangle, input_square, input_rectangle, input_circle
from chose_oper import chose_operation,validate_operation_input, print_result


def main():
    msg = """1 - Тругольник,
    2 - Квадрат,
    3 - Прямоугольника,
    4 - Круг,
    5 - Журнал,
    0 - Exit"""
    oper = input(msg)

    while oper != "0":
        match oper:
            case "1": # Треугольник.
                a,b,c = input_triangle()
                operation = validate_operation_input()

                if operation == "1":
                    result = tr_perimeter(a,b,c)
                    add_to_journal("Треугольник", "Периметр", result)

                    print_result("Треугольника", "Периметр", result)
                    
                elif operation == "2":
                    result = tr_area(a,b,c)
                    add_to_journal("Треугольник", "Площадь", result)

                    print_result("Треугольника", "Площадь", result)

            case "2": # Квадрат.
                a = input_square()
                operation = validate_operation_input()

                if operation == "1":
                    result = sq_perimeter(a)
                    add_to_journal("Квадрат", "Периметр", result)

                    print_result("Квадрата", "Периметр", result)
                    
                elif operation == "2":
                    result = sq_area(a)
                    add_to_journal("Квадрат", "Площадь", result)

                    print_result("Квадрата", "Площадь", result)                 

            case "3": # Прямоугольник.
                a,b = input_rectangle()
                operation = validate_operation_input()

                if operation == "1":
                    result = rec_perimeter(a,b)
                    add_to_journal("Прямоугольник", "Периметр", result)

                    print_result("Прямоугольника", "Периметр", result)
                    
                elif operation == "2":
                    result = rec_area(a,b)
                    add_to_journal("Прямоугольник", "Площадь", result)

                    print_result("Прямоугольника", "Площадь", result)
                    
            case "4": # Круг.
                r = input_circle()
                operation = validate_operation_input()

                if operation == "1":
                    result = cir_perimeter(r)
                    add_to_journal("Круг", "Длина окружности", result)

                    print_result("Круга", "Периметр", result)
                    
                elif operation == "2":
                    result = cir_area(r)
                    add_to_journal("Круг", "Площадь", result)

                    print_result("Круга", "Периметр", result)
                    
            case "5": # Журнал
                print("--------------------------------")
                print("Журнал запросов:")

                if not get_my_journal():
                    print("Журналл пустой.")
                else:
                    for entry in get_my_journal():
                        print(f"Запрос: {entry['shape']} - {entry['operation']} - "
                            f"{entry['result']} {entry['units']}" )
                
                print("--------------------------------")

            case _:
                print("--------------------------------")
                print("Некорректные данные!")
                print("--------------------------------")

        oper = input(msg)

main()

