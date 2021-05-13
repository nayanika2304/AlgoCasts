class Solution(object):
    def check_valid_parenthesis(self,str):
        stack = []
        paren = {
            '[' : ']',
            '{' : '}',
            '(' : ')',
        }
        inv_paren = {v:k for k,v in paren.items()}

        for c in str:
            if c in paren:
                stack.append(c)
            elif c in inv_paren:
                if  len(stack) == 0 or stack[-1] != inv_paren[c]:
                    return False
                else:
                    stack.pop()
        return len(stack) == 0

print(Solution().check_valid_parenthesis('(){([])}'))
#True
print(Solution().check_valid_parenthesis('(){(['))
#False

