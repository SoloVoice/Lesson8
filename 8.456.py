class MyException(Exception):
    def __init__(self, text):
        self.text = text


class Store:
    stored = []
    store = {
        "Принтеры": 0,
        "Сканнеры": 0,
        "Ксероксы": 0
    }
    departments_to_move = ["Бухгалтерия", "Отдел маркетинга", "Отдел продаж", "Склад"]

    def to_store(self, eq):
        eq.current_location = "Склад"
        self.stored.append(eq)
        if eq.eq_type == "Принтер":
            self.store["Принтеры"] += 1
        elif eq.eq_type == "Сканнер":
            self.store["Сканнеры"] += 1
        elif eq.eq_type == "Ксерокс":
            self.store["Ксероксы"] += 1

    def move_to(self, input_id, input_dep):
        c = 0
        cc = 0
        for xl in self.stored:
            if xl.eq_id == input_id:
                if xl.eq_type == "Принтер":
                    self.store["Принтеры"] -= 1
                elif xl.eq_type == "Сканнер":
                    self.store["Сканнеры"] -= 1
                elif xl.eq_type == "Ксерокс":
                    self.store["Ксероксы"] -= 1
                xl.current_location = self.departments_to_move[input_dep - 1]
                self.stored.pop(c)
                cc += True
            else:
                cc += False
            c += 1
        if cc < 1:
            print("=============================================================\n"
                  "Оборудование с таким инвентаризационным номером не существует\n"
                  "=============================================================\n")
        else:
            print(f"Оборудование успешно перемещено в подразделение {self.departments_to_move[input_dep - 1]}\n")

    def stored_list(self):
        print("===================================")
        print("В данный момент на складе хранятся:")
        print("===================================")
        for ii in self.stored:
            print(f"{ii.eq_type} с инвентаризационным номером {ii.eq_id}, "
                  f"текущее место хранения: {ii.current_location}")
        print("")
        print("==========================================")
        print("Складированно единиц оборудования по типу:")
        print("==========================================")
        for iii in self.store.items():
            print(f"{iii[0]}: {iii[1]} шт.")
        print("")


class OfficeEquipment:
    country_of_origin = "Китай"
    produced_in_year = 2020
    current_location = "не распределено"

    def __init__(self, eq_id):
        self.eq_id = eq_id


class Printer(OfficeEquipment):
    eq_type = "Принтер"
    manufacturer = "Samsung"


class Scanner(OfficeEquipment):
    eq_type = "Сканнер"
    manufacturer = "HP"


class Xerox(OfficeEquipment):
    eq_type = "Ксерокс"
    manufacturer = "Xerox"


"""Инициация объектов"""
store = Store()
printer_1 = Printer(10001)
printer_2 = Printer(10002)
printer_3 = Printer(10003)
scanner_1 = Scanner(20001)
xerox_1 = Xerox(30001)
xerox_2 = Xerox(30002)
"""На пустой склад размещено следующее оборудование"""
store.to_store(printer_1)
store.to_store(printer_2)
store.to_store(printer_3)
store.to_store(scanner_1)
store.to_store(xerox_1)
store.to_store(xerox_2)
"""Тестовый список со всем заведенным оборудованием, чтоб можно было смотреть перемещения"""
test_list = [printer_1, printer_2, printer_3, scanner_1, xerox_1, xerox_2]
"""Взаимодействие с пользователем"""
print("\nДоступ до конкретных экземпляров оборудования происходит через инвентаризационный номер.\n"
      "Для навигации используйте указания системы.\n"
      "Для завершения программы используйте комманду 'ex'\n")
while True:
    user_select_action = input("Какую операцию Вы хотите произвести?\n"
                               "1 - посмотреть текущий склад (узнать инвентаризационные номера)\n"
                               "2 - переместить оборудование между подразделениями\n"
                               "3 - вывести информацию по размещению всего оборудования\n"
                               "Введите число обозначающее команду: ")
    print("")
    if user_select_action == "ex":
        print("Программа завершена")
        break
    try:
        for ch in list(user_select_action):
            if ord(ch) < 49 or ord(ch) > 51 or len(user_select_action) > 1:
                raise MyException("============================================================="
                                  "===========================\n"
                                  "Неверная команда. используйте цифры от 1 до 3 и команду 'ex' "
                                  "что-бы выйти из программы\n"
                                  "============================================================="
                                  "===========================\n")
    except (ValueError, MyException) as error:
        print(error)
        continue
    if int(user_select_action) == 1:
        store.stored_list()
    elif int(user_select_action) == 2:
        while True:
            user_input = input("Для возврата в предыдущее меню используйте комманду 'ex'\n"
                               "Введите инвентаризационный номер для перемещения: ")
            if user_input == "ex":
                print("Возврат в меню\n")
                break
            user_input_dest = int(input("Куда переместить оборудование? Введите значение отвечающее отделу"
                                        "\n1 - Бухгалтерия\n2 - Отдел маркетинга\n3 - Отдел продаж\n4 - Склад\n"))
            if user_input_dest == 4:
                for o in test_list:
                    if o.eq_id == int(user_input):
                        store.to_store(o)
                        print(f"Оборудование {o.eq_type} c инвентаризационным номером {o.eq_id} "
                              f"успешно размещено на Складе\n")
            else:
                store.move_to(int(user_input), int(user_input_dest))
    elif int(user_select_action) == 3:
        print("============================================")
        print("Полная информация об оборудовании в наличии.")
        print("============================================")
        for i in test_list:
            print(f"Инвентаризационный номер оборудования: {i.eq_id}")
            print(f"Тип оборудования: {i.eq_type}")
            print(f"Производитель: {i.manufacturer}")
            print(f"Страна производства: {i.country_of_origin}")
            print(f"Год производства: {i.produced_in_year}")
            print(f"Текущее складирование: {i.current_location}")
            print("")
