class Solution(object):
    def trap(self, height):
        """
        READING THROUGH THE QUESTION:
        len(height) >= 0
        width of each "bar" is 1
        amount of "water" that it can "trap after raining"
        ==
        the number of heights above each "floor" piece that have bar on the left and right of them
        trapped: the absence of value where there is at least that value on both sides 
        3 1 2 => trap 1 at index 1
        returning the number of trapped elements => only need to keep track of the number of trap
        """
        num_trapped = 0
        l,r = 0, len(height) - 1
        max_left = height[l]
        max_right = height[r]
        while (l < r):
            if max_left < max_right:
                stored = max_left - height[l]
                l += 1
                max_left = max(height[l], max_left)
                if (stored > 0):
                    num_trapped += stored
            else:
                stored = max_right - height[r]
                r -= 1
                max_right = max(height[r], max_right)
                if (stored > 0):
                    num_trapped += stored


        return num_trapped
