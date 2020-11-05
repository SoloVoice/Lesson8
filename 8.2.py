class MyException(Exception):
    def __init__(self, text):
        self.text = text


user_input_1 = int(input("Что делим?: "))
user_input_2 = int(input("НА что делим?: "))
try:
    if user_input_2 == 0:
        raise MyException("Нельзя днлить на ноль!")
except (ZeroDivisionError, MyException) as error:
    print(error)
else:
    print(user_input_1 / user_input_2)
