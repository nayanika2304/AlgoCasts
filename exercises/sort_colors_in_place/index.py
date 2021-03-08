class Solution(object):
    def sort_in_place(self, colors):
        left = 0
        current = 0
        right = len(colors) - 1

        while current <= right:
            if colors[current] == 0:
                colors[left], colors[current] = colors[current],colors[left]
                left += 1
                current += 1
            elif colors[current] == 2:
                colors[right],colors[current]  = colors[current],colors[right]
                right -= 1
            else:
                current += 1
        return colors

    def sortColors(self,colors):
        res = []
        dic1 = {}

        for color in colors:
            dic1[color] = dic1.get(color,0) + 1

        for color in range(len(set(colors))):
            res += [color] * dic1.get(color)

        return res

print(Solution().sort_in_place([0, 2, 1, 0, 1, 1, 2]))
