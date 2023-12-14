def generator():
    n = 1

    while True:
        yield f'{n}, a'
        n += 1
        yield 33

obj = generator()

print(next(obj))
print(99999999999999999999)
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))

while True:
    print(next(obj))