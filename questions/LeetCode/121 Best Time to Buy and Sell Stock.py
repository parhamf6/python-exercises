class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        prices1 = sorted(prices)
        lowest = prices1[0]
        il = prices.index(lowest)
        prices2 = prices[il:]
        prices3 = sorted(prices2)
        highest = prices3[-1]
        if highest>lowest:
            x = (int(highest)-int(lowest))
            return x
        elif highest <= lowest:
            return 0
        