num1 = int(input("enter first number"))
num2 = int(input("enter second number"))

try:
    print(num1/num2)
except ZeroDivisionError:
    print("sorry, u cant devide by zero")
finally:
    print("excuted")