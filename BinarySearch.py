def main(arr, num):
    arr = sorted(arr)
    low = 0
    up = len(arr) - 1

    while low <= up: 
        mid = (low + up) // 2        
        if arr[mid] == num:
            return mid
        elif arr[mid] < num:
            low = mid + 1
        else:
            up = mid - 1

num = 78

result = main([11,23,45,53,78,80,94], num)

if result != -1:
    print(f"Element {num} found at index {result}")
else:
    print(f"Element {num} not found in the array")
