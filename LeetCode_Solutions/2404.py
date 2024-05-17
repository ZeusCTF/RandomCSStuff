from collections import defaultdict
def main(nums):
    even_nums = {}
    for num in nums:
        if num % 2 == 0:
            even_nums[num] = 1 + even_nums.get(num, 0)
    if even_nums:
        print(max(even_nums))
        print(sorted(even_nums))
        print(sorted(even_nums, key=even_nums.get))
        return min(even_nums)
    else:
        return -1
#main([0,1,2,2,4,4,1])

def test(nums):
    d = defaultdict(int)
    for num in nums:
        d[num] += 1
    print(d.items())
    print(sorted(d))
test([0,1,2,2,4,4,1])