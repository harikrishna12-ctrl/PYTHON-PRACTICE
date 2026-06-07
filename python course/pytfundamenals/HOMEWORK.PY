username=input("enter your name: ");
age=int(input("Enter our age"));
print("hello",username,"you are",age,"years old");

a=input("enter a number: ");
b=input("enter another number: ");

a,b=b,a;
print("after swapping:");
print("a=",a);
print("b=",b);