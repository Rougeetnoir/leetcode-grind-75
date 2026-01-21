# class Solution:
#     def maxProfit(self, prices: list[int]) -> int:
#         #brutal force
#         # max = 0
#         # n = len(prices)
#         # for i in range(n):
#         #     for j in range(i+1, n):
#         #         if prices[j] - prices[i] > max:
#         #             max = prices[j] - prices[i]
#         # return max

        #slicing
prices = [7,1,5,3,6,4]

# print(prices[1:])
# max = 0
for i in range(len(prices)):
    print(prices[i+1:])
#     if prices[i] < max(prices[i:]):
#         max = max(prices[i:]) - prices[i]

# print max
