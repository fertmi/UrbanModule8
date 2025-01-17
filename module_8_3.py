class Car:
    def __init__(self, model:str, vin:int, auto_number:str):
        self.model = model
        self.__vin = vin if self.__is_valid_vin(vin) else None
        self.__number = vin if self.__is_valid_numbers(auto_number) else None

    def __is_valid_vin(self, vin_number):
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber('Некорректный тип vin номер')
        elif not 1000000 <= vin_number <= 9999999:
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
        else:
            return True

    def __is_valid_numbers(self, numbers):
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers('Некорректный тип vin номер')
        elif not len(numbers) == 6:
            raise IncorrectCarNumbers('Неверная длина номера')
        else:
            return True

class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message

class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message

#Основная программа
try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')