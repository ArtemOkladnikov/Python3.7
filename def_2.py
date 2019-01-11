def func(*args):
    a = {}
    for element in args:
        if str(type(element)) not in a.keys():
            a[str(type(element))] = 1
        else:
            a[str(type(element))] += 1
    return a

test = func(1,2, "Hello", [1,2,3], {"name":"Artem"})
print(test)

