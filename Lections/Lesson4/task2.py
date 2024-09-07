data = [25, -42, 146, 73, -100, 12]
print(list(map(str, data))) # ['25', '-42', '146', '73', '-100', '12']
print(max(data, key=lambda x: -x)) # -100
print(*filter(lambda x: not x[0].startswith('__'), globals().items())) # ('data', [25, -42, 146, 73, -100, 12])
