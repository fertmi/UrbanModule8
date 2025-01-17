class Car:
    def __init__(self, model, vin, auto_number):
        self.model = model
        self.__vin = vin if self.__is_valid_vin(vin) else None
        self.__number = vin if self.__is_valid_numbers(auto_number) else None

    def __is_valid_vin(self, vin_number):
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber('Некорректный тип vin номера')
        elif not 1000000 <= vin_number <= 9999999:
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
        else:
            return True

    def __is_valid_numbers(self, numbers):
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
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

#Функция регистрация автомобиля
def register_car(serial_number_car, model, vin, auto_number):
    try:
        serial_number_car = Car(model, vin, auto_number)
    except IncorrectVinNumber as exc:
        print(exc.message)
    except IncorrectCarNumbers as exc:
        print(exc.message)
    else:
        print(f'{serial_number_car.model} успешно создан')


#Основная программа
register_car('first','Model1', 1000000, 'f123dj')
register_car('second','Model2', 300, 'т001тр')
register_car('third','Model3', 2020202, 'нет номера')
register_car('fourth','Model4', 7020202, 908301)
register_car('fifth','Model5', '9000000', 'Т165ТХ')
register_car('sixth','Model6', 9999999, 'Т251ТХ')