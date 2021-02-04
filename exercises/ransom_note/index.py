from collections import defaultdict

class Solution(object):
    # the solution below is O(n*m)
    def ransom_note(self, arr, w):
        flag = False
        for i in range(0,len(w)):
            if w[i] in arr:
                flag = True
            else:
                flag = False
        return flag

    #The solution below is O(n) + O(m)
    def canSpell(self, magazine, note):
        letters = defaultdict(int)
        for c in magazine:
            letters[c] += 1

        for c in note:
            if letters[c] <= 0:
                return False
            letters[c] -= 1

        return True

dict = ['A', 'B', 'C', 'D', 'E', 'F']
word = 'CAT'
print(Solution().ransom_note(dict,word))
# True
