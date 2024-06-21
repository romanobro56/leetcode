class Solution(object):
    def maxArea(self, height):
        current_max = 0
        l,r = 0,len(height)-1
        while (l<r):
            width = r - l
            surface = min(height[r],height[l])
            area = surface * width
            if area > current_max:
                current_max = area
            if height[r] > height [l]:
                l += 1
            else:
                r -= 1


        return current_max