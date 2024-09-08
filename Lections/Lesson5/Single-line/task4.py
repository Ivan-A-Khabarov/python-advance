def gen(a: int, b: int) -> str:
    if a > b:
        a, b = b, a
    for i in range(a, b + 1):
        yield str(i)


for item in gen(10, 1):
    print(f'{item = }')

# item = '1'
# item = '2'
# item = '3'
# item = '4'
# item = '5'
# item = '6'
# item = '7'
# item = '8'
# item = '9'
# item = '10'