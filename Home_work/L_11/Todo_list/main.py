from package_classes.to_do_list_class import TodoList
from package_classes.app import App


def main():
    td1 = TodoList()
    app = App(td1)
    app.Run()


if __name__ == "__main__":
    main()

