def sum(a,b,c):
    s=a+b+c/3
    return s

ans=sum(3,4,3)
print(ans)

def sum(a,b,c=1):
    s=a+b+c/3
    return s

ans=sum(3,4)
print(ans)
