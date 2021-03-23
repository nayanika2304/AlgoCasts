class Solution(object):
    def buy_and_sell(self,arr):
        max_profit = 0

        for i in range(len(arr)):
            for j in range(i,len(arr)):
                max_profit = max(max_profit,arr[j] - arr[i])

        return max_profit

    def buy_sell_2(self,arr):
        max_current_price = 0
        max_profit = 0

        for i in arr[::-1]:
            max_current_price = max(max_current_price,i)
            max_profit = max(max_profit,max_current_price - i)

        return max_profit

print(Solution().buy_sell_2([9, 11, 8, 5, 7, 10]))
