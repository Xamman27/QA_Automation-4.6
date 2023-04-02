from datetime import time


def test_dark_theme_by_time():
    """
    Протестируйте правильность переключения темной темы на сайте в зависимости от времени
    """
    current_time = time(hour=23)
    # TODO переключите темную тему в зависимости от времени суток (с 22 до 6 часов утра - ночь)

    is_dark_theme = automation_enable_dark_theme_by_time(current_time)
    assert is_dark_theme is True


def automation_enable_dark_theme_by_time(current_time):
    if time(hour=22) <= current_time or current_time <= time(hour=6):
        is_dark_theme = True
    else:
        is_dark_theme = False
    return is_dark_theme


def test_dark_theme_by_time_and_user_choice():
    """
    Протестируйте правильность переключения темной темы на сайте
    в зависимости от времени и выбора пользователя
    """
    current_time = time(hour=16)
    dark_theme_enabled_by_user = True
    # TODO переключите темную тему в зависимости от времени суток,
    #  но учтите что темная тема может быть включена вручную

    is_dark_theme = automation_enable_dark_theme_by_time_by_user(current_time, dark_theme_enabled_by_user)
    assert is_dark_theme is True


def automation_enable_dark_theme_by_time_by_user(current_time, dark_theme_enabled_by_user):
    if dark_theme_enabled_by_user is True:
        is_dark_theme = True
        return is_dark_theme
    else:
        if time(hour=22) <= current_time or current_time <= time(hour=6):
            is_dark_theme = True
        else:
            is_dark_theme = False
    return is_dark_theme



def test_find_suitable_user():
    """
    Найдите нужного пользователя по условиям в списке пользователей
    """
    users = [
        {"name": "Oleg", "age": 32},
        {"name": "Sergey", "age": 24},
        {"name": "Stanislav", "age": 15},
        {"name": "Olga", "age": 45},
        {"name": "Maria", "age": 18},
    ]


    # TODO найдите пользователя с именем "Olga"
    suiable_user = [i for i in users[:] for y in i.values() if y == 'Olga'][0]
    assert suiable_user == {"name": "Olga", "age": 45}


    # TODO найдите всех пользователей младше 20 лет
    suiable_users = [i for i in users[:] for key, value in i.items() if key == 'age' and int(value) < 20]
    assert suiable_users == [
        {"name": "Stanislav", "age": 15},
        {"name": "Maria", "age": 18},
    ]


# Сделайте функцию, которая будет печатать
# читаемое имя переданной ей функции и значений аргументов.
# Вызовите ее внутри функций, описанных ниже
# Подсказка: Имя функции можно получить с помощью func.__name__
# Например, вызов следующей функции должен преобразовать имя функции
# в более читаемый вариант (заменить символ подчеркивания на пробел,
# сделать буквы заглавными (или первую букву), затем вывести значения всех аргументов этой функции:
# >>> open_browser(browser_name="Chrome")
# "Open Browser [Chrome]"


def test_readable_function():
    open_browser(browser_name="Chrome")
    go_to_companyname_homepage(page_url="https://companyname.com")
    find_registration_button_on_login_page(page_url="https://companyname.com/login", button_text="Register")


def open_browser(browser_name):
    print('\n')
    actual_result = get_name_funct(open_browser, browser_name)
    assert actual_result == "Open Browser [Chrome]"


def go_to_companyname_homepage(page_url):
    actual_result = get_name_funct(go_to_companyname_homepage, page_url)
    assert actual_result == "Go To Companyname Homepage [https://companyname.com]"


def find_registration_button_on_login_page(page_url, button_text):
    actual_result = get_name_funct(find_registration_button_on_login_page, page_url, button_text)
    assert actual_result == "Find Registration Button On Login Page [https://companyname.com/login, Register]"


def get_name_funct(name_f, *arg_func):
    name = []
    upper_flag = True# флаг для Апер символа, изначально True, на первой итерации мы сделаем первый знак Апер
    for i in list(name_f.__name__):# функция __name__ возвращает str,через list делаем список для удобства цикла
        if upper_flag:
            name.append(str(i).upper())
            upper_flag = False
        elif i == '_':
            name.append(' ')
            upper_flag = True
        else:
            name.append(i)
    name = ''.join(name) + ' ' + '[' + ', '.join(arg_func) + "]"
    print(name)
    return name
