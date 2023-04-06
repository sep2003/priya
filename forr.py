n=6
m=n
for index in range (1,n+1,2):
    s=m//2
    for i in range(s):
        print(" ",end="")
    m=m-2
    for index_1 in range(index) :
        print("*",end="")
    print()