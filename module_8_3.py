class Car:
    serial_car = 1
    def __init__(self, model, vin, auto_number):
        self.model = model
        self.__vin = vin if self.__is_valid_vin(vin) else None
        self.__number = vin if self.__is_valid_numbers(auto_number) else None
        self.serial_car += 1

    def __str__(self):
        return f'Модель: {self.model}, зарегистрирована под номером: {self.serial_car}'

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
def register_car(model, vin, auto_number):
    try:
        object_car = Car(model, vin, auto_number)
    except IncorrectVinNumber as exc:
        print(exc.message)
        return f'{model} не зарегистрирована по причине: {exc.message}'
    except IncorrectCarNumbers as exc:
        print(exc.message)
        return f'{model} не зарегистрирована по причине: {exc.message}'
    else:
        print(f'{object_car.model} успешно создан')
    return object_car

#Основная программа
first=register_car('Model1', 1000000, 'f123dj')
second=register_car('Model2', 300, 'т001тр')
third=register_car('Model3', 2020202, 'нет номера')
fourth=register_car('Model4', 7020202, 908301)
fifth=register_car('Model5', '9000000', 'Т165ТХ')
sixth=register_car('Model6', 9999999, 'Т251ТХ')
print(sixth)
print(second)