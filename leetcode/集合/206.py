def matrixScore(A):
    row, col = len(A), len(A[0])
    # 第一列非0的行->翻转
    for i in range(row):
        if A[i][0] == 0:
            for j in range(col):
                A[i][j] = 1 - A[i][j]
    # 辅助函数，返回某列是否0>1
    def helper(_col):
        count_0, count_1 = 0, 0
        for i in range(row):
            if A[i][_col] == 1:
                count_1 += 1
            else:
                count_0 += 1
        return count_0 > count_1
    # 从第二列开始看，如果0比1多则该列翻转
    for i in range(1,col):
        if helper(i):
            for j in range(row):
                A[j][i] = 1 - A[j][i]
    # 统计结果
    re = 0
    for i in range(row):
        for j in range(col):
            re += A[i][col-j-1]*2**j
    return re

a = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
print(matrixScore(a))