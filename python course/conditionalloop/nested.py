username =input("enter username: ")
password =input("enter password: ") 

if (username=="admin" and password=="admin123"):
    print("welcome",username)

else:
    if (username!="admin" and password=="admin123"):
        print("invalid username but correct password")
    else:
        print("invalid username and password")