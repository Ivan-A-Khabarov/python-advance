import sys

while True:
    input_data = input('Введите данные: ')
    try:
        int_value = int(input_data)
        if int_value > 0:
            print(int_value)
            break
        else:
            raise ValueError()
    except ValueError:
        pass

    try:
        float_value = float(input_data)
        if float_value >= 0:
            print(float_value)
            break
        else:
            print(float_value)
            break
    except ValueError:
        pass

    if isinstance(input_data, str):
        lowercase_value = input_data.lower()
        if 'a' <= lowercase_value[0] <= 'z':
            print(lowercase_value)
            break
        else:
            print(lowercase_value)
            break

sys.exit(0)