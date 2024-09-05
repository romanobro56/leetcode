class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        first = 0
        last = len(nums)
        middle = len(nums) // 2

        while (nums[middle] != target):
            new_middle = 0
            if (nums[middle] > target):
                last = middle
                new_middle = (first + last) // 2
            elif (nums[middle] < target): 
                first = middle 
                new_middle = (first + last) // 2
            
            if (new_middle == middle):
                return -1
            else:
                middle = new_middle

        return middle 
