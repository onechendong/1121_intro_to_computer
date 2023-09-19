num = input("please inpput a number :")
print("please inpput a number :"+num)
if int(num)%2==0:
    print("this is even")
else:
    print("this is odd")
    
first_letter = input("please input your student ID first character :")
print("please input your student ID first character :"+first_letter)
ID_num = input("please input your student ID last 8 numbers :")
print("please input your student ID last 8 numbers :"+ID_num)
if int(ID_num)%2==0:
    print("your student ID number is even")
else:
    print("your student ID number is odd")
print("your student ID is :"+first_letter+ID_num)