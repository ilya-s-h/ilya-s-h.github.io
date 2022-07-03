# Установка virtualenv:
#
# pip install virtualenv
#
# Создание виртуального окружения:
#
# virtualenv virtual_env
#
# Активания virtual_env:
#
# virtual_env\Scripts\activate.bat
#
# Деактивация virtual_env:
#
# virtual_env\Scripts\deactivate.bat

def number_of(numb: int, numb_type=""):
    """Функция, которая принимает на вход целое число от 0 до 9 и
         возвращает имя этого числа, а если второй входной аргумент n_type
         имеет значение bin, oct, hex, функция преобразует это число в бинарную,
         восьмеричную или шестнадцатеричную систему счисления.
    """

    # Проверка, что numb - целое число
    if isinstance(numb, int):

        # Проверка, что numb входит в [0;9]
        if numb >= 0 and numb <= 9:

            # Второй аргумент имеет значение bin
            if numb_type == "bin":
                result =  format(numb, 'b')

            # Второй аргумент имеет значение oct
            elif numb_type == "oct":
                result = format(numb, 'o')

            # Второй аргумент имеет значение hex
            elif numb_type == "hex":
                result = format(numb, 'x')

            # Второй аргумент - пустая строка
            elif numb_type == "":
                result = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"][numb]

            # numb - не bin/oct/hex
            else:
                raise ValueError("numb value must be: bin/oct/hex")

        # numb вне диапазона допустимых значений
        else:
            raise ValueError("numb must be in range [0;9]")

    # numb - не int
    else:
        raise TypeError("type of numb must be int")

    return result
