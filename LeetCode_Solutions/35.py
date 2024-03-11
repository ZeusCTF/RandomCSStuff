def main(nums, target):
    low = 0
    up = len(nums) - 1

    while low <= up: 
        mid = (low + up) // 2        
        if nums[mid] == target:
            print(nums.index(target))
            return
        elif nums[mid] < target:
            low = mid + 1
        else:
            up = mid - 1
    if low > up:
        print(mid + 1)
main([1,3,5,6], 7)