def main(nums, target):
    low = 0
    up = len(nums) - 1

    while low <= up:
        mid = (low + up) // 2
        if nums[mid] == target:
            print(mid)
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            up = mid - 1

    if low > up and target > nums[up]:
        print(up + 1)
        return up + 1
    elif low > up and target < nums[low]:
        print(low)
        return low
    else:
        print(0)
        return 0

main([1,3], 2)
