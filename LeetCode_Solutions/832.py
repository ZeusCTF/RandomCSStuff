def main(image):
    ans = []
    for arr in image:
        arr.reverse()
        ans.append([1 - x for x in arr])
    print(ans)
main([[0,1,1,1,1],[0,1,1,0,0],[0,1,1,1,1],[1,0,0,1,0],[0,0,0,0,1]])
