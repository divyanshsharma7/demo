def find_max_min(arr):
    max_num = min_num = arr[0]  # Initialize with first element

    for num in arr:
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num

    return max_num, min_num

nums = [3, 1, 7, 9, 2, 5]
print(find_max_min(nums))  


# def find_max_min(arr):
#     max_num=min_num=arr[0]
    
#     for num in arr:
#         if num > max_num:
#             max_num=num
#         if num < min_num:
#             min_num=num
#     return max_num, min_num

# nums=[4,5,7,8,3]
# print(find_max_min(nums))
