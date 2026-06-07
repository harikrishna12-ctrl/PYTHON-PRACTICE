colour=input("enter a colour: ")

#we are using match case statement to check the colour
match colour:
    case "red":
        print("you have selected red")
    case "blue":
        print("you have selected blue")
    case "green":
        print("you have selected green")
    case _:
        print("invalid colour")