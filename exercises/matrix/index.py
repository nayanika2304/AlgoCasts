class Solution(object):
    def spiralOrder(self,matrix):
        if not matrix:
            return matrix
        else:
            start_row = 0
            end_row = len(matrix) - 1
            start_column = 0
            end_column = len(matrix[0]) - 1
            spiral = []
            while start_row <= end_row and start_column <= end_column:

                # top row
                for i in range(start_column,end_column +1):
                    spiral.append(matrix[start_row][i])

                start_row += 1

                # right column
                for i in range(start_row,end_row+1):
                    spiral.append(matrix[i][end_column])

                end_column -= 1

                #bottom row
                for i in range(end_column,start_column-1,-1):
                    spiral.append(matrix[end_row][i])

                end_row -=1

                # left column
                for i in range(end_row,start_row-1,-1):
                    spiral.append(matrix[i][start_column])

                start_column += 1

            return spiral


grid = [[1,  2,  3,  4,  5],
        [6,  7,  8,  9,  10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20]]

print(Solution().spiralOrder(grid))
