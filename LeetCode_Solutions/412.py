def main(i):
    ans = []
    for i in range(1, i + 1):
        if i % 3 == 0 and i % 5 == 0:
            ans.append('FizzBuzz')
        elif i % 3 == 0:
            ans.append('Fizz')
        elif i % 5 == 0:
            ans.append('Buzz')
        else:
            ans.append(str(i))
        
    print(ans)


main(25)