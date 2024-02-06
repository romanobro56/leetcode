class Solution(object):
    def removeDuplicates(self, nums):
        lastKnownUnique = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[lastKnownUnique]:
                lastKnownUnique += 1
                nums[lastKnownUnique] = nums[i]
        return lastKnownUnique + 1
