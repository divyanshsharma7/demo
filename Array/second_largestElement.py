# 📌 Day 1: List Practice Problems
# 1️⃣ Find the Second Largest Number in a List
# 🔹 Problem: Given a list of numbers, find the second largest number.
# 📌 Example:

# Input: [10, 5, 20, 8, 25, 15]  
# Output: 20  
# 👉 Hint: Sort the list or track two max values while looping.

# my try


# list =[10,5,20,8,25,15]
# list.sort()
# print(list)
# print(f"Second largest number of the list is :- {list[4]}")


# Another form

def second_largest(nums):
    first, second = float('-inf'), float('-inf')  # Initialize with negative infinity
    for num in nums:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
    return second

nums = [10, 5, 20, 8, 25, 15]
print(f"Second largest number of the list is: {second_largest(nums)}")
