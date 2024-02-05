def main(s):
    ans = 0
    for letter in s[::-1]:
        if letter != ' ':
            ans += 1
        else:
            break
    print(ans)
        


main('luffy is still joyboy')
