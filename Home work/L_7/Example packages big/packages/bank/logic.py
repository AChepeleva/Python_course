
data = []

def add(value):
    data.append(value)
    print(f"Bank added: {value}")

def changes(value):
    if value in data:
        print(f"Bank changed: {value}")
    else:
        print(f"Bank value {value} not found for change")

def delete(value):
    if value in data:
        data.remove(value)
        print(f"Bank deleted: {value}")
    else:
        print(f"Bank value {value} not found")

def show():
    print("Bank data:", data)


if __name__ == "__main__":
    print("I prefer to be a module")
else:
    print("I like to ba f module")

    