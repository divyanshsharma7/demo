def sort_DFA(arr):
    low, mid, high = 0, 0, len(arr) - 1
    
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]  # Swap 0 to left
            low += 1  # low = low+1
            mid += 1   # mid = mid+1
        elif arr[mid] == 1:
            mid += 1  # Leave 1s in the middle
        else:
            arr[mid], arr[high] = arr[high], arr[mid]  # Swap 2 to right
            high -= 1

arr = [2, 0, 2, 1, 1, 0]
sort_DFA(arr)
print(arr) 
