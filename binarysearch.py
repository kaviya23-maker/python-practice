def binary_search(arr, key):
    low, high = 0, len(arr)-1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1

arr = list(map(int, input("Enter sorted array elements: ").split()))
key = int(input("Enter key to search: "))
result = binary_search(arr, key)
print("Found at index", result if result != -1 else "Not Found")
