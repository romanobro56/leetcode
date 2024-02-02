class Solution(object):
  def productExceptSelf(self, nums):
    pre = 1
    post = 1
    output = []
    for i in range(len(nums)):
      output.append(pre)
      pre *= nums[i]
    for i in range(len(nums)):
      output[len(nums) -i -1] *= post
      post *= nums[len(nums) -i -1]

    return output