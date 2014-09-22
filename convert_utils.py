from collections import OrderedDict

ARABIC_TO_ROMAN = OrderedDict([
    (1000, 'M'),
    (900, 'CM'),
    (500, 'D'),
    (400, 'CD'),
    (100, 'C'),
    (90, 'XC'),
    (50, 'L'),
    (40, 'XL'),
    (10, 'X'),
    (9, 'IX'),
    (5, 'V'),
    (4, 'IV'),
    (1, 'I'),
])


class InvalidProvidedValue(Exception):
    pass


def arabic_to_roman(initial_arabic_number):
    if initial_arabic_number < 1:
        raise InvalidProvidedValue('Initial number must be > 1')
    elif initial_arabic_number > 3999:
        raise InvalidProvidedValue('Initial number must be < 4000')

    result = []
    for num, rom in ARABIC_TO_ROMAN.iteritems():
        while initial_arabic_number >= num:
            initial_arabic_number -= num
            result.append(rom)
    return ''.join(result)


def roman_to_arabic(initial_roman_number):
    initial_roman_number = initial_roman_number.upper()

    result = i = 0
    for num, rom in ARABIC_TO_ROMAN.iteritems():
        l = len(rom)
        while initial_roman_number[i:i+l] == rom:
            result += num
            i += l

    if result == 0:
        raise InvalidProvidedValue('Wrong initial number')
    # `arabic_to_roman` is a way to always get the right value.
    # We should check that it's result is equal to initial value.
    # If not, the result is wrong.
    elif result > 0 and arabic_to_roman(result) != initial_roman_number:
        raise InvalidProvidedValue('Something wrong in initial number')

    return result


def choice_convert_function(number):
    # try convert to integer..
    try:
        return arabic_to_roman(int(number))
    # ..seems to be roman number
    except ValueError:
        return roman_to_arabic(number)
