# Binary search

nums = [1, 3, 65, -1, 23, 455, 66666, 7, 9, 3, 0]
nums.sort()  # sorting
print(nums)

search_for = 9  # what we are looking for

lowest = 0
highest = len(nums) - 1
index = None  # place for future index

while (lowest <= highest) and (index is None):
    mid = (lowest + highest) // 2  # middle

    if nums[mid] == search_for:
        index = mid

    else:
        if search_for < nums[mid]:
            # looking on the left of the list
            highest = mid - 1
        else:
            # on the right
            lowest = mid + 1

print("Index of the", search_for, " is: ", index)
