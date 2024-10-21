from string import ascii_letters


def checkstr(text: str):
    return ''.join(let for let in text.lower() if let in ascii_letters + ' ')


if __name__ == '__main__':
    print(checkstr(''))