'''
general principles of backtracking/recursion

1) Our choice
    Place a "(" or ")"
2) Our constraints
    if there is an opening bracket, there is a closed bracket
3) Our goal
    n*2 placements
'''
class Solution(object):
    def _genParensHelper(self, n, left, right, str):
        if left + right == 2 * n:
            return [str]

        result = []
        if left < n:
            result += self._genParensHelper(n, left + 1, right, str+'(')

        if right < left:
            result += self._genParensHelper(n, left, right + 1, str+')')
        return result

    def genParens(self, n):
        return self._genParensHelper(n, 0, 0, '')


print(Solution().genParens(3))
# ['((()))', '(()())', '(())()', '()(())', '()()()']
