def main(candidates, target):
    ans = []

    for num in candidates:
        if target % num == 0:
            ans.append([num] * int(target / num))
    print(ans)

main([2,3,6,7], 7)