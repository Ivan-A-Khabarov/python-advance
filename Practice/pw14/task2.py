from string import ascii_letters

def check_str(text: str):
    """
    >>> check_str('hello')
    'hello'
    >>> check_str('Hello')
    'hello'
    >>> check_str('Hello!!!')
    'hello'
    >>> check_str('Привет world')
    ' world'
    >>> check_str('привет World!')
    ' world'
    """
    alph = ascii_letters + ' '
    result = ''
    for let in text:
        if let in alph:
            result += let
    return result.lower()


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)

print(check_str('Привет hello'))