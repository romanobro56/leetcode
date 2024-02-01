class Solution(object):
    def topKFrequent(self, nums, k):
        nums_dict = {}
        for item in nums: 
            if item in nums_dict:
                nums_dict[item] += 1
            else:
                nums_dict[item] = 1
        top_nums = sorted(nums_dict, key=nums_dict.get, reverse=True)[:k]
        return top_nums