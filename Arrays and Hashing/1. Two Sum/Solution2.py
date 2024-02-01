class Solution(object):
  def twoSum(self, nums, target):
    checkedNums = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in checkedNums:
            return [checkedNums[complement], i]
        checkedNums[num] = i