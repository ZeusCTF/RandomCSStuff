def main(matrix):
    ans = []
    x = len(matrix)
    #print(x)
    for i in range(0,x):
        temp = []
        count = 0
        while count <= len(matrix):
            print(count)
            print('---')
            print(i)
            temp.append(matrix[count][i])
            count += 1
        ans.append(temp)
    print(ans)

main([[1,2,3],[4,5,6]])
#[1,2,3],[4,5,6],[7,8,9]
#-> [1,4,7],[2,5,8],[3,6,9]