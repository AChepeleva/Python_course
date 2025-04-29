#
def funny():
    print("fun"*100)

if __name__ == "__main__":
    print("fun - запущен по F5 или руками")
    funny()
else:
    print("fun - запущен через import в другой модуль")

