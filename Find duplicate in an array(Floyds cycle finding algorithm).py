def findDuplicate(nums):
    slow,fast=0,0
    while True:
        slow=arr[slow]
        fast=arr[arr[fast]]
        if slow==fast:
            break
    slow2=0
    while True:
        slow=arr[slow]
        slow2=arr[slow2]
        if slow==slow2:
            return slow


arr = [1, 2, 1, 2, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 9]
duplicate_element = findDuplicate(arr)
print("Duplicate element:", duplicate_element)
