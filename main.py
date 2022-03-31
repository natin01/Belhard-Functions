# task 1
def concat(*args, r: bool = False):
    mystr = ''
    if r == True:
        for a in reversed(args):
            mystr = mystr + a
    else:
        for a in (args):
            mystr = mystr + a
    return mystr


res = concat("Hello", " ", "world", " ", "finally")
print(res)
res = concat("Hello", " ", "world", " ", "finally", r=True)
print(res)


# task 2
def fibonacci(n: int) -> int:
    if n == 1:
        return 1
    if n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(7))


# task 3 (incomplete)
def inspect(func):
    print("Args",)
    return func

myFunc = inspect(concat)
res = myFunc("Hello", " ", "world", " ", "finally")
print(res)
