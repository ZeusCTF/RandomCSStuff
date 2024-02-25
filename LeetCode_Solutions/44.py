def main(digits):
    inc = ''
    ans = []
    for num in digits:
        inc += str(num)
    
    inc = int(inc) + 1

    for digit in str(inc):
        ans.append(int(digit))

    return ans
main([1,2,3])