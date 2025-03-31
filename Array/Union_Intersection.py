def find_union_intersection(arr1, arr2):
    i, j = 0, 0  # Initialize two pointers
    union = []
    intersection = []

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            if not union or union[-1] != arr1[i]: 
                union.append(arr1[i])
            i += 1
        elif arr1[i] > arr2[j]:
            if not union or union[-1] != arr2[j]:  
                union.append(arr2[j])
            j += 1
        else:
            if not union or union[-1] != arr1[i]:  
                union.append(arr1[i])
            intersection.append(arr1[i])  
            i += 1
            j += 1

    while i < len(arr1):
        if not union or union[-1] != arr1[i]:
            union.append(arr1[i])
        i += 1

    while j < len(arr2):
        if not union or union[-1] != arr2[j]:
            union.append(arr2[j])
        j += 1

    return union, intersection

arr1 = [1, 2, 4, 5, 6]
arr2 = [2, 3, 5, 7]
union, intersection = find_union_intersection(arr1, arr2)
print("Union:", union)         
print("Intersection:", intersection)  
