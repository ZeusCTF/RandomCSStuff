def main(nums):
    y = []
    x = []
    for num in nums:
        if num % 2 == 0:
            x.append(num)
        else:
            y.append(num)
    print(x + y)
main([1,2,3,4])