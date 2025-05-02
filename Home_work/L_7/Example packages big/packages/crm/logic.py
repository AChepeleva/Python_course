
data = []

def add(value):
    data.append(value)
    print(f"CRM added: {value}")

def changes(value):
    if value in data:
        print(f"CRM changed: {value}")
    else:
        print(f"CRM value {value} not found for change")

def delete(value):
    if value in data:
        data.remove(value)
        print(f"CRM deleted: {value}")
    else:
        print(f"CRM value {value} not found for deletion")

def show():
    print("CRM data:", data)


if __name__ == "__main__":
    print("I prefer to be a module")
else:
    print("I like to ba f module")

    