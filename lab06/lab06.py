def gcd(a, b):#find gcd
    if(a!=0 and b!=0):
        if(a%b==0):
            return(b)
        elif(a%b==b):
            return 1
        else:
            return(gcd(b, a%b))
    else:#a=0 or b=0
        return 0
        
def PrintGcd(num3, num1, num2):#function is created to print the output
    if(num3==0):#one of input=0
        print("0 沒有gcd")
    elif(num3==1):#Coprime
        print(f"{num1} 和 {num2} 互質")
    else:#!Coprime
        print(f"{num1} 和 {num2} 的gcd= {num3}")

ans1 = gcd(80, 20)
ans2 = gcd(10, 0)
ans3 = gcd(19, 20)
PrintGcd(ans1, 80, 20)
PrintGcd(ans2, 10, 0)
PrintGcd(ans3, 19, 20)


        
