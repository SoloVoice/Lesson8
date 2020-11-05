class Date:
    def __init__(self, date):
        self.date_valid(date)

    @classmethod
    def str_to_int(cls, row_date):
        in_date = row_date.split("-")
        int_date = []
        for i in in_date:
            int_date.append(int(i))
        return cls(int_date)

    @staticmethod
    def date_valid(date):
        day, month, year = date
        if 0 < day < 32 and 0 < month < 13 and year == 20:
            day = str(day).zfill(2)
            month = str(month).zfill(2)
            year = str(year).zfill(2)
            print(f"Текущая дата {day} / {month} / {year}")
        else:
            print("Где твой DeLorean доктор Эммет Браун? Прекращай эти эксперименты со временем! Неверный формат даты.")


a = Date.str_to_int(input("Введите текущую дату в формате дд-мм-гг: "))
