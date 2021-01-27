class Solution(object):
    def rotate(self, matrix):
        for j in range(0, len(matrix)):
            for i in range(j + 1, len(matrix[j])):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = tmp
            matrix[j].reverse()
        return matrix

print(Solution().rotate([[1,2],[3,4]]))
