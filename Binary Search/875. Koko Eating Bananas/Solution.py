class Solution(object):
    def minEatingSpeed(self, piles, h):
        def feasible(k): 
            return sum(ceil(1.0 * piles[i] / k) for i in range(len(piles))) <= h
        
        l, r = 1, 10 ** 9
        while l <= r:
            mid = (l + r) // 2
            if feasible(mid):
                r = mid - 1
            else:
                l = mid + 1

        return l