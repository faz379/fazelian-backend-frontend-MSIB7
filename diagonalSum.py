# %%
class Solution:
    def diagonalSum(self, mat):
        res, n = 0, len(mat)
        for i in range(n):
            res += mat[i][i]
            res += mat[i][n-i-1]
        return res - mat[n//2][n//2] if n % 2 else res

# %%
sol = Solution()

print(sol.diagonalSum([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]))

print(sol.diagonalSum([
    [ 1,  2,  3,  4],
    [ 5,  6,  7,  8],
    [ 9, 10, 11, 12],
    [13, 14, 15, 16],
]))



