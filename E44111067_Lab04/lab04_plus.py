#turn "input(string)" into list 
nums = list(input("輸入的list為:"))
nums.remove("[")
nums.remove("]")
nums = "".join(nums)
nums = nums.split(", ")
for i in range(len(nums)):
    nums[i] = int(nums[i])
#get val
val = int(input("要刪除的數字是:"))
#show the input
print(f"輸入的list為: {nums}, 要刪除的數字是: {val}")
#delete val
while (val in nums):
    nums.remove(val)
#show the result
print("\n刪除後!\n")
print(f"list長度剩下: {len(nums)}, list變成: {nums}")
