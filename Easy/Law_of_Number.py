from numpy.random import randn
N=1000
counter = 0
for i in randn(N):
    if (i>-1 and i<1):
        counter=counter +1
answer=counter/N
print(answer)