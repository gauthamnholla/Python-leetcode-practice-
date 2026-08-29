class Solution:
    def minPrice(self, prices, discounts):

        prices.sort(reverse=True)
        discounts.sort(reverse=True)

        price = 0.0

        n = len(prices)
        m = len(discounts)

        for i in range(min(n, m)):
            price += prices[i] * (100 - discounts[i]) / 100

        for i in range(m, n):
            price += prices[i]

        return price