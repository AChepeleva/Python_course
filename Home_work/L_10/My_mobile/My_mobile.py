class MobilePhone:
    """Класс мобильный телефон.
    number - номер телефона;
    switch -флаг включен телефон или нет (True - включен, False - выключен).
    """

    def __init__(self, number):
        """Функция для инициализации объекта MobilePhone."""
        self.number = number
        self.switch = False


    def turn_on(self):
        """Функция для включения мобильного телефона."""
        self.switch = True
        return f"mobile phone {self.number} is turned on"


    def turn_off(self):
        """Функция для выключения мобильного телефона."""
        self.switch = False
        return f"mobile phone {self.number} is turned off"


    def call(self, cally):
        """Функция для звонка по указанному номеру."""
        if self.switch:
            return f"calling {cally}"
        else:
            return "Mobile phone is turned off. Can't make a call."
        
