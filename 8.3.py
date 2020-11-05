class MyException(Exception):
    def __init__(self, text):
        self.test = text


some_list = []
print("Для выхода из программы используйте комманду 'stop'")
while True:
    check = True
    user_input = input("Введите элемент списка: ")
    if user_input == "stop":
        break
    user_input_check = list(user_input)
    if user_input_check.count("-") > 0:
        user_input_check.remove("-")
    if user_input_check.count(".") > 0:
        user_input_check.remove(".")
    for i in user_input_check:
        try:
            if ord(i) < 48 or ord(i) > 57:
                check = False
                raise MyException("Это был не Нескафе! Можно вводить только цифры")
        except (ValueError, MyException) as error:
            print(error)
            break
    if check is False:
        continue
    else:
        if list(user_input).count("."):
            user_input = float(user_input)
        else:
            user_input = int(user_input)
        some_list.append(user_input)
print(some_list)
