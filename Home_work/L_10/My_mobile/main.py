from My_mobile import MobilePhone

def main():

    phone = MobilePhone("375291234455")

    print(phone.turn_on())
    print(phone.call("375290001212"))
    print(phone.turn_off())


if __name__ == "__main__":
    main()
