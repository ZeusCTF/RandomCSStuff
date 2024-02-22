def main(arr):
    arr.sort()
    ans = []
    min_dif = 99**99
    for i in range(1, len(arr)):
        prev = i - 1
        diff = abs(arr[i] - arr[prev])
        if diff < min_dif:
            min_dif = diff
            ans = [[arr[prev],arr[i]]]
        elif diff == min_dif:
            ans.append([arr[prev],arr[i]])
    print(ans)