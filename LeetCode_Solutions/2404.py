
def main(nums):
    maximum = -1
    even_nums = {}
    prev_value = 0
    prev_key = max(nums)

    for num in nums:
        if num % 2 == 0:
            even_nums[num] = 1 + even_nums.get(num, 0)
    if even_nums:
        for key, value in even_nums.items():
            
            if value > prev_value:
                prev_value = value
                maximum = key
            if value == prev_value and key < prev_key:
                maximum = key
                prev_key = key


    return maximum
main([0,1,2,0,0,0,2,4,4,1])
