import matplotlib.pyplot as plt
a=float(input("Enter a: "))
b=float(input("Enter b: "))
m=(a+b)/2
X=(a,m,b)
Y=(0,1,0)
plt.plot(X,Y)
plt.show()


x=float(input("Enter the element: "))
if x<=a:
    mem = 0
elif x>a and x<=m:
    mem = (x-a)/(m-a)
elif x>m and x<b:
    mem = (b-x)/(b-m)
else:
    mem=0
    
print("Membership : ",mem)