def calculator(a, b, operation):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero"
    else:
        return "Invalid operation"

#take input
a=int(input("enter  number 1: "))
b=int(input("enter 2nd number : "))
operation= input("enter the operation : ")

ans = calculator(a,b,operation)
print(ans)