x= int(input("Enter number of terms in series"))
n1=0
n2=1
n3=0

Series= [n1,n2]

for i in range(1,x):
    n1=n2
    n2=n3
    n3= n1+n2
    Series.append(n3)

print(Series)
