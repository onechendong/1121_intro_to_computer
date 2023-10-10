dict0 = {}
for i in range(4):#creat 4 keys and values
    key_temp = input("Enter keys: ")
    print(f"Enter keys: {key_temp}"")
    value_temp = input("Enter values: ")
    print(f"Enter values: {value_temp}")
    dict0[key_temp] = (value_temp).split(", ")#turn string into list
print(f"dict0 = {dict0}")
