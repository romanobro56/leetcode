class Solution(object):
    def threeSum(self, nums):
        res = []
        nums.sort()

        for i in range(len(nums)-2):

            if len(res) > 0 and nums[i] == res[-1][0]:
                continue

            complement = 0 - nums[i]
            j = i + 1
            k = len(nums) - 1

            while j < k:
                if nums[j] + nums[k] > complement:
                    k -= 1
                elif nums[j] + nums[k] < complement: 
                    j += 1
                else:
                    res.append([nums[i],nums[j],nums[k]])
                    j += 1
                    while nums[j] == nums[j-1] and j < k:
                        j += 1

        return res

        
