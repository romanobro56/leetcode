class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        prefix = [0] * (len(arr) + 1)
        for i, num in enumerate(arr):
            prefix[i+1] = prefix[i] + num

        max_odd_subarray_len = len(arr)
        if len(arr) % 2 == 0:
            max_odd_subarray_len -= 1

        sum = 0
        print(prefix)
        for i in range(max_odd_subarray_len,0,-2):
            # i starts at the largest odd subarray length and decreases until 1
            for j in range(i, len(prefix)):
                # j should span the indecies of prefix array that sum
                # all the subarrays with minimum length i => from prefix[j] to len(prefix)
                sum += prefix[j] - prefix[j-i]

        return sum 

