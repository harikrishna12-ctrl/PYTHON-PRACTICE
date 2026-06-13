# salary = int(input("enter your salary: "))

# if salary<30000:
#     print("your take will 5% of your money")

# elif 30000<=salary<=70000:
#     print("your tax rate will be 15%")

# else:
#     print("your tax rate will be 25%")

# a= int(input("enter your no : "))
# b= int(input("enter your no : "))

# sum =a+b

# for i in range(min(a,b),max(a,b)+1):
#     if i%2==0:
#         print(i)
  

# num= input("enter the number : ")
# count=0
# for t in num:
#     print(t)
#     count = count+1

# print(count)    



#my home work
# Even or Odd


# num =3
# s=1

# for i in range(1,num+1):
#   s=s*i


# print(s)

# people = ["Ravi", "Arun", "Ravi", "Kiran", "Arun", "Manoj"]
# anull_set = set()

# for name in people:
#     anull_set.add(name)
    
# print(anull_set)  

# Q1. College Event Registration

# A college event has the following registrations:
registrations = [
    "Rahul", "Anil", "Rahul",
    "Kiran", "Manoj", "Anil",
    "Pooja", "Kiran", "Ravi"
]
# null_set=set()
# for names in registrations:
#     null_set.add(names)
    
# print(null_set)    


#printing people who registered only once
# frec={}
# for names in registrations:
#      frec[names]=frec.get(names,0)+1
 

# for name,count in frec.items():
#      if(count==1):
#           print(name)


marks = {
    "Ravi": 78,
    "Anil": 35,
    "Kiran": 92,
    "Pooja": 45,
    "Manoj": 33
}


max_marks=max(marks,key=marks.get)
print(marks)

print("most issued:",max_marks)