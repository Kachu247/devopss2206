
try:
    a = int(input("enter number: "))
    b = int(input("enter number: "))
    print(a / b)
except ZeroDivisionError as e:
    print("you tried to divide by zero")
    print(e.args)
except ValueError as e:
    print("bad input")
    print(e.args)
except BaseException as e:
    print(e.args)
print("aviel")