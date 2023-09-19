a = input("請輸入第一個邊長:")
print("請輸入第一個邊長:"+a)
b = input("請輸入第二個邊長:")
print("請輸入第二個邊長:"+b)
c = input("請輸入第三個邊長:")
print("請輸入第三個邊長:"+c)
a = int(a)
b = int(b)
c = int(c)
if a+b>c and b+c>a and a+c>b:
    if a==b and b==c:
        print("這是一個正三角形")
    elif a==b or b==c or c==a:
        print("這是一個等腰三角形")
    else:
        print("這是一個一般三角形")
else:
    print("這三個邊長不能構成一個合法的三角形")