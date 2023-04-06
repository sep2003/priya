n=int(input("Enter the value of n :"))

i=0
while i<n:
    s=0
    while s>0:
        s=s-1
    j=n
    while j>i:
        print("*",end="")
        j=j-1
    print("")
    i=i+1


