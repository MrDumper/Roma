def inch_to_cm(value): #дюймы в сантметры
    const = 2.54
    return round(value*const, 2)


def cm_to_inch(value):
    const = 2.54
    return round(value/const, 2)


def miles_to_km(value): #мили в километры
    const = 1.609
    return round(value*const, 2)


def km_to_miles(value):
    const = 1.609
    return round(value/const, 2)


def lb_to_kg(value): #фунты в килограммы
    const = 2.205
    return round(value/const, 2)


def kg_to_lb(value):
    const = 2.205
    return round(value*const, 2)


def ounce_to_gram(value): #унции в граммы
    const = 28.35
    return round(value*const, 2)


def gram_to_ounce(value):
    const = 28.35
    return round(value/const, 2)


def gallon_to_liter(value): #галлоны в литры
    const = 3.785
    return round(value*const, 2)


def liter_to_gallon(value):
    const = 3.785
    return round(value/const, 2)


def pint_to_liter(value): #пинты в литры
    const = 2.113
    return round(value/const, 2)


def liter_to_pint(value):
    const = 2.113
    return round(value*const, 2)


def wanna_to_continue():
    while True:
        print('Желаете продолжить?')
        print('1. Да')
        print('2. Нет(Выход)')
        choice = input()
        if choice == '1':
            print('')
        elif choice == '2':
            exit()
        else:
            print('Выбрана неверная опция попробуйте еще раз')


def menu():
    wanna_to_input = 'Введите значение\n'
    functions = {
        '1': inch_to_cm,
        '2': cm_to_inch,
        '3': miles_to_km,
        '4': km_to_miles,
        '5': lb_to_kg,
        '6': kg_to_lb,
        '7': ounce_to_gram,
        '8': gram_to_ounce,
        '9': gallon_to_liter,
        '10': liter_to_gallon,
        '11': pint_to_liter,
        '12': liter_to_pint
    }
    print('Добро пожаловать')
    god_var = True
    while True:
        print('Выберите интересующую вас опцию:')
        print('1. Дюймы в сантиметры')
        print('2. Сантиметры в дюймы')
        print('3. Мили в километры')
        print('4. Километры в мили')
        print('5. Фунты в килограммы')
        print('6. Килограммы в фунты')
        print('7. Унции в граммы')
        print('8. Граммы в унции')
        print('9. Галлон в литры')
        print('10. Литры в галлоны')
        print('11. Пинты в литры')
        print('12. Литры в пинты')
        print('0. Выход')
        choice = (input())
        if choice in functions:
            var = int(input(wanna_to_input))
            print(functions[choice](var))
            wanna_to_continue()
        elif choice == '0':
            break
        else:
            print('Неверная операция, попробуй еще раз', end='\n\n')


menu()
