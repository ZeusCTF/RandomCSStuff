def main(matrix):
    ans = []
    x = len(matrix)
    n = len(matrix[0])
    for i in range(0, n):
        app = []
        for j in range(0,x):
            app.append(matrix[j][i])
        ans.append(app)
    
    print(ans)



main([[1,2,3],[4,5,6]])
#[1,2,3],[4,5,6]

#[1,2,3],[4,5,6],[7,8,9]
#-> [1,4,7],[2,5,8],[3,6,9]