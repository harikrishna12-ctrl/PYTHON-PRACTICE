age=int(input("enter your age: "))
if age >= 18:
    print("you are an adult")
    print("this will always execute")   
elif (age >= 13 and age < 18):
    print("you are a teenager")
else:
    print("you are a child")