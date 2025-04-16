import matplotlib.pyplot as plt
print("Enter a: ")
a=input()
a=float(a)
print("Enter b: ")
b=input()
b=float(b)
print("Enter c: ")
c=input()
c=float(c)
print("Enter d: ")
d=input()
d=float(d)
X=(a,b,c,d)
Y=(0,1,1,0)
plt.plot(X,Y)
plt.show()



x=float(input("Enter the element: "))
if x <= a:
    mem = 0
elif x > a and x <= b :
    mem = (x - a) / (b - a)
elif x > b and x < c :
    mem = 1
elif x >= c and x <= d :
    mem = (d - x) / (d - c)
else :    
    mem=0
    
print("Membership :",mem)    