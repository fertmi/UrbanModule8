def add_everything_up(a,b):
    try:
        return f'результат сложения: {round(a + b, 3)}'
    except TypeError:
        return f'результат сложения разных типов: {str(a) + str(b)}'

#Основная программа
print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))