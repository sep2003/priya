import spe 
print("\t\t My python shape calculator:\t\t")
print("\t\t\t Welcome \t\t\t")
print(" 1.Area of Rectangle\n","2.Area of Square\n","3.Area of Triangle\n","4.Area of Circle\n","5.Area of Cube")
choice=input("Enter your choice[1,2,3,4,5]:")

if choice in ["1","2","3","4","5"]:
    if choice=="1":
        print("\t\t Rectangle:\t\t")
        l=int(input("Enter the length of the Rectangle :"))
        b=int(input("Enter the breath of the Rectangle :"))
        print("Area of the Rectange is:"+str(spe.rec(l,b)))
    elif choice=="2":
        print("\t\tSquare:\t\t")
        a=int(input("Enter the area of the square :"))
        print("Area of the square "+str(spe.sqr(a)))
    elif choice=="3":
        print("\t\tTriangle:\t\t")
        b=int(input("aenter the base of the triangle :"))
        h=int(input("Enter the height of the triangle :"))
        print("Area of Triangle is "+str(spe.tri(b,h)))
    elif choice=="4":
        print("\t\tCircle:\t\t")
        r=int(input("Enter the radius of the Circle :"))
        print("Area of Circle is :"+str(spe.cir(r)))
    elif choice=="5":
        print("\t\tCube:\t\t")
        a=int(input("Enter the area of the Cube:"))
        print("Area of the Cube is :"+str(spe.cub(a)))
else:
    print("Invalid choice.")   
    print("Please enter the choice in above equation: ") 
        
        
        
        
        
        
        
        