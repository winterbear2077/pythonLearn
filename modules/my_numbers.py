def add(*args):
    if len(args) < 1:
        return
    return sum([i for i in args])


print(add(1, 2, 3, 4))
