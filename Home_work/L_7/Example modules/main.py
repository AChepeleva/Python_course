#

import sport_data as sdl
#from fun import funny

def main():
    oper = input("1 - add, 2 - show, 3 - delete, -1 - exit")
    while oper != "-1":
        user_data = input("-->")
        match oper:
            case "1":
                sdl.Add(user_data)
            case "2":
                sdl.Show(user_data)
            case "3":
                sdl.Delete(user_data)
            case _:
                #funny()
                print("Ne ponimau")

        oper = input("1 - add, 2 - show, 3 - delete, -1 - exit")  


main()

