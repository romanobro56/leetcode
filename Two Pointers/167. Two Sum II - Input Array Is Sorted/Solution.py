class Solution(object):
    def twoSum(self, numbers, target):
        left = 0 
        right = len(numbers) - 1

        while right > left:
            checkSum = numbers[left] + numbers[right]

            if checkSum > target:
                right -= 1
            elif checkSum < target:
                left += 1
            else:
                return [ left + 1, right + 1 ]
