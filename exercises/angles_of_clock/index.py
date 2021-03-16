class Solution(object):
    def calculate_angle(self,h,m):
        hour_angle = (360/(12 * 60.0)) * (h * 60 + m)
        minute_angle = 360/60.0 * m
        angle = abs(hour_angle - minute_angle)
        return min(angle, 360-angle)

print(Solution().calculate_angle(3,15))
# ??
print(Solution().calculate_angle(3,00))
# 90
