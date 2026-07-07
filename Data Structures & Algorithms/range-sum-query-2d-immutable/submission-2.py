class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        n = len(matrix)
        m = len(matrix[0])

        self.dp = [[0 for j in range(m+1)] for i in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,m+1):
                self.dp[i][j] = matrix[i-1][j-1] + self.dp[i][j-1] + self.dp[i-1][j] - self.dp[i-1][j-1]

    def sumRegion(self, x1: int, y1: int, x2: int, y2: int) -> int:
        return self.dp[x2+1][y2+1] - self.dp[x1][y2+1] - self.dp[x2+1][y1] + self.dp[x1][y1]

        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)