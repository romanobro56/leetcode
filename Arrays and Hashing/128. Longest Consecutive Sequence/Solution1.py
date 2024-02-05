class Solution(object):
    def longestConsecutive(self, nums):

        # Recursive check function will return length of sequence of given value
        def check(num_to_check):
            running_total = 1
            while num_to_check in nums:
                nums.remove(num_to_check)
            if num_to_check + 1 in nums:
                running_total += check(num_to_check + 1)
            if num_to_check - 1 in nums:
                running_total += check(num_to_check - 1)
            

            return running_total

        # main longest consecutive code
        longest = 0
        while len(nums) != 0:
            sequence_length = check(nums[0])
            if sequence_length > longest:
                longest = sequence_length

        return longest
