class Solution(object):
    def lengthOfLongest_substring(self,str):
        letter_pos = {}
        start = -1
        end = 0
        max_length = 0
        while end < len(str):
            c = str[end]
            if c in letter_pos:
                start = max(start,letter_pos[c])
            max_length = max(max_length,end-start)
            letter_pos[c] = end
            end+=1
        return max_length



print(Solution().lengthOfLongest_substring('aabcbbeacc'))
