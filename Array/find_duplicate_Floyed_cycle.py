# using  Floyd’s Cycle Detection (Tortoise and Hare) Method

def find_duplicate(nums):
    slow = fast = nums[0]

    # Phase 1: Detect cycle
    while True:
        slow = nums[slow]  # Move one step
        fast = nums[nums[fast]]  # Move two steps
        if slow == fast:  
            break

    # Phase 2: Find start of cycle (duplicate number)
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    return slow

nums = [1, 3, 4, 2, 2]
print(find_duplicate(nums))  



# def find_duplicates(nums):
#     slow=fast=nums[0]
    
#     while True:
#         slow=nums[slow]
#         fast=nums[nums[fast]]
#         if slow==fast:
#             break
        
#     slow=nums[0]
#     while slow!=fast:
#         slow=nums[slow]
#         fast=nums[fast]
#     return slow

# nums=[1,3,4,2,2]
# print(find_duplicates(nums))