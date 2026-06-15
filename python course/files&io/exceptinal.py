try :
    x= int(input("enter the number"))
    ans=10/x

except ZeroDivisionError:
    print("divide by 0 is not allowed")


except ValueError:
    print(f"invalid number")


else :
    print(f"ans ={ans}")

finally:
    print("end of program")