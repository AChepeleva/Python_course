# CRDU
# Creat - Add
# Read - Show
# Delete - Delete

def Add(data):
    print(data, "was created!")


def Show(data):
    print("Show data:")
    print(data)


def Delete(data):
    print(data, "was removed!")


if __name__ == "__main__":
    print("sport_data - запущен по F5 или руками")
    print()
    test_date = 'gvfdcs'
    Add(test_date)
    Show(test_date)
    Delete(test_date)
else:
    print("sport_data - запущен через import в другой модуль")
    