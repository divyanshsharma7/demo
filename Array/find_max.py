# 📌 Practice Problem
# 🔹 Find the Maximum Number in a List
# Input: [5, 12, 8, 3, 25, 7]
# Output: 25

def find_max(nums):
    max_num = nums[0]  # Assume first element is the max
    for num in nums:
        if num > max_num:
            max_num = num  # Update max if a bigger number is found
    return max_num

# Example usage
nums = [5, 12, 8, 3, 25, 7]
print("Maximum number:", find_max(nums))

