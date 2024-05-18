
def main(nums):
    max = -1
    even_nums = {}
    for num in nums:
        if num % 2 == 0:
            even_nums[num] = 1 + even_nums.get(num, 0)
    if even_nums:
        for key, value in even_nums.items():
            print(key, value)
            print('-' * 50)
            print(value, max)
            print()
            print()
            if value > max:
                max = key
    print(max)
    return max
main([0,1,2,0,0,0,2,4,4,1])