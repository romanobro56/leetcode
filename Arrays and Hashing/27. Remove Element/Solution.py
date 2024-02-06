class Solution(object):
    def removeElement(self, nums, val):
        
        index = 0
        for item in nums:
            if item is not val:
                nums[index] = item
                index +=1
        return index


        """
        [3,0,0] => [0,0,_] k=2
        [0,0,3] => [0,0,_] k=2
        [0,3,0] => [0,0,_] k=2
        [3,3,3] => [_,_,_] k=0
        [0,0,0] => [0,0,0] k=3
        [0,3,3] => [0,_,_] k=1
        [3,3,0] => [0,_,_] k=1

        
        
        """