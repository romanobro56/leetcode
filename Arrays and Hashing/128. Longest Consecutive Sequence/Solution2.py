class Solution(object):
    def longestConsecutive(self, nums):
        nums_set = set(nums)
        longest_sequence_len = 0

        for item in nums_set:
            if (item - 1) not in nums_set:
                this_sequence_len = 1
                current_value = item
                while (current_value + 1) in nums_set:
                    current_value += 1
                    this_sequence_len += 1
                if this_sequence_len > longest_sequence_len:
                    longest_sequence_len = this_sequence_len

        return longest_sequence_len
            