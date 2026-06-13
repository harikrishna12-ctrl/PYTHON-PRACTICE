marks =[ 99,43,56,"reddy",45,65,434]
print(marks)
print(len(marks))
print(marks[4])

# #the list is mutable
marks[3]=43
print(marks[3])
#list has som method 0r functions

# 1)l.append(var) 
#adding a value at the end
num =[32,45,65,65]
num.append(43)
print(num)

# 2) inserting at what index we needed
nums =[43,43,5356,64334,4]
nums.insert(4,545)
print(nums)


# 3) sorting list
num =[3,43,54,65,6,5,6,7]
num.sort()
print(num)

num.sort(reverse=True)
print(num)

num.reverse()
print(num)

