import math
print ("Hello world")

x=2
print(x)
type(x)

A=5
B=10
C= A+B
print(C)
D=B/A
print (D)
import math
E=round(math.sqrt(60))
print(E)

greeting = "Hello"
name = "Rachel"
message = greeting + " " + name
print(message)

#Boolean/Logical
F=4>5
print(F)
G = not(10>100)
print(G)
H = type(F)
print(H)
I = F or G
print(I)
J = F and G
print(J)

#while loop
counter = -10
while counter < 12:
    print(counter)
    counter = counter + 1

#for loop
for i in range(5):
    print("Hello", i)

mylist = [10,100,1000]
for jj in mylist:
    print("Hello", jj)

#if-else
from numpy.random import randn
x=randn()
if x >1:
    answer= "greater than 1"
elif x > -1:
    answer="Number is between 1 and -1"
else:
    answer="Less than -1"
print(x)
print(answer)



