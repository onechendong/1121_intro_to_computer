def function(str) -> List[str]:
    if len(str) == 1:
        return [str]

    permutations = []
    for i, char in enumerate(str):#將index為i的char挑出
        for perm in function(str[:i] + str[i+1:]):#將剩下的字元們接起來當新的str丟回function裡
            permutations.append(char + perm)#丟回function後，產生的permutations中的每一個elements前面接上一開始挑出的char
    return permutations

input_string = input()
permutations = function(input_string)
permutations = list(set(permutations))#刪掉permutations中重複出現的element
print(permutations)