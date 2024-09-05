class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        temp_stack = [0]
        output = [0] * len(temperatures)
        for i in range(1,len(temperatures)):
            while(len(temp_stack) > 0 and temperatures[i] > temperatures[temp_stack[-1]]):
                j = temp_stack.pop()
                output[j] = i - j
            temp_stack.append(i)

        return output