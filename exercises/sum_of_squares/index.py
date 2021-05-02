#https://www.youtube.com/watch?v=1xfx6M_GqFk&ab_channel=TECHDOSE

#Minimum number of squares whose sum equals to given number n

# A dynamic programming based Python
# program to find minimum number of
# squares whose sum is equal to a
# given number
from math import ceil, sqrt

# Returns count of minimum squares
# that sum to n
def getMinSquares(n):

    # Create a dynamic programming table
    # to store sq and getMinSquares table
    # for base case entries
    dp = [0, 1, 2, 3]

    # getMinSquares rest of the table
    # using recursive formula
    for i in range(4, n + 1):
        
        # max value is i as i can always
        # be represented as 1 * 1 + 1 * 1 + ...
        dp.append(i)

        # Go through all smaller numbers
        # to recursively find minimum
        for x in range(1, int(ceil(sqrt(i))) + 1):

            temp = x * x
            if temp > i:
                break
            else:
                dp[i] = min(dp[i], 1 + dp[i-temp])

    # Store result
    return dp[n]

# Driver code
print(getMinSquares(6))
