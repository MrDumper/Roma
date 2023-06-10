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


def wanna_to_continue(choice=True):
    while True:
        print('Желаете продолжить?')
        print('1. Да')
        print('2. Нет(Выход)')
        choice = input()
        if choice == '1':
            print('')

            return True
        elif choice == '2':
            break
            return False
        else:
            print('Выбрана неверная опция попробуйте еще раз')


def menu():
    print('Добро пожаловать')
    god_var = True
    while god_var is True:
        wanna_to_input = "Введите значение"
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
        if choice == '1':
            print(wanna_to_input)
            print(f'{inch_to_cm(int(input()))}  cm')
            god_var = wanna_to_continue()
        elif choice == '2':
            print(wanna_to_input)
            print(f'{cm_to_inch(int(input()))} inch')
            god_var = wanna_to_continue()
        elif choice == '3':
            print(wanna_to_input)
            print(miles_to_km(int(input())), ' km')
            god_var = wanna_to_continue()
        elif choice == '4':
            print(wanna_to_input)
            print(km_to_miles(int(input())), ' miles')
            god_var = wanna_to_continue()
        elif choice == '5':
            print(wanna_to_input)
            print(lb_to_kg(int(input())), ' kg')
            god_var = wanna_to_continue()
        elif choice == '6':
            print(wanna_to_input)
            print(kg_to_lb(int(input())), ' lb')
            god_var = wanna_to_continue()
        elif choice == '7':
            print(wanna_to_input)
            print(ounce_to_gram(int(input())), ' gram')
            god_var = wanna_to_continue()
        elif choice == '8':
            print(wanna_to_input)
            print(gram_to_ounce(int(input())), ' ounce')
            god_var = wanna_to_continue()
        elif choice == '9':
            print(wanna_to_input)
            print(gallon_to_liter(int(input())), ' liter')
            god_var = wanna_to_continue()
        elif choice == '10':
            print(wanna_to_input)
            print(liter_to_gallon(int(input())), ' gallon')
            god_var = wanna_to_continue()
        elif choice == '11':
            print(wanna_to_input)
            print(pint_to_liter(int(input())), ' liter')
            god_var = wanna_to_continue()
        elif choice == '12':
            print(wanna_to_input)
            print(liter_to_pint(int(input())), ' pint')
            god_var = wanna_to_continue()
        elif choice == '0':
            break
        else:
            print('Неверная операция, попробуй еще раз', end='\n\n')


menu()
