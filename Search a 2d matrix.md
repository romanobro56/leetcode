1. Take notes on the problem

You must write a solution in `O(log(m * n))` time complexity.

Each row is sorted in non-decreasing order.
    - doesn't that just mean increasing !?

return true if the target is within the matrix

-----
2. Theorize on how problem is solved 

You must write a solution in O(log(m * n)) time complexity.

-----
3. Learn optimal solution
    3.5 Write out solution

nah f that imma try it

```py
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        self.b, self.t = 0, len(matrix) - 1
        self.mid = 0
        while self.b <= self.t:
            self.mid = (self.t + self.b) // 2
            # if the item at index matrix[mid][0] is greater than the target then 
            # it must be in a row before mid or nonexistant
            # we must find what t and b converge on therefore it is unlikely there will be a shortcut in the loop
            if matrix[self.mid][0] == target:
                return True
            elif matrix[self.mid][0] > target:
                self.t = self.mid - 1
            else:
                self.b = self.mid + 1

        # the goal is to get mid to converge on the greatest element of all the 
        # first numbers of each arr that is less than the target
        
        print(self.mid)
        
        self.l, self.r = 0, len(matrix[0]) - 1
        self.mid_2 = 0

        while self.l <= self.r:
            self.mid_2 = (self.r + self.l) // 2
            if matrix[self.t][self.mid_2] == target:
                return True
            elif matrix[self.t][self.mid_2] > target:
                self.r = self.mid_2 - 1
            else:
                self.l = self.mid_2 + 1

        return False

```

-----
4. Take notes on what you didn't know, mark reading as todo if necessary

Uhh I was really close the first time

but it should be constant brush up on how the mid and indecies selection works especially if you writing it

-----
5. Metanotes

Maybe I should have just used that one for learning? Like no matter what I see in the problem and how easy it seems to solve just learn it if you thought you were gonna learn it initially? Maybe. I ended up using chat. Maybe I could have sketched out the traversal of mid across the arrays and figured it out but that's not how we should be thinking in the interview so idk.
