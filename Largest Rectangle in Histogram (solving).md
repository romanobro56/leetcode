Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram

1 <= heights.length <= 10^5
0 <= heights[i] <= 10^4

rectangle could be horizontal or vertical or both

first thing comes to mind is sorting by height and then calculating the area for each possible as it ascends but then when it starts to descend we know we've found the largest

The rectangle could be horizontal or vertical or both

Stack

heights = [2,1,5,6,2,3]

5 x 2 = 10

1 x 6 = 6

Ohh you move inward from the outside

heights[i] could be zero, therefore there could be gaps in the middle of something, not very helpful 

Even if you identify something in the middle that could be the greatest there could be something to the left or the right of that no?

Okay say we start at the right and the left. There's one gap at 3n/4. We can't assume that the largest rectangle would be on the left just because it has more horizontal area at the base

do we have to break it down into constituent parts? like dfs?

If it was dfs how would it be...

Imagine you start at the base. n width with zero height. Then you can move deeper. either there is n width with 1 height or m widths with m_i heights

Then from there you move on, breaking up each m into the next widest sections each with their own heights that we don't know yet

How can we organize the data like this?

1 we know n width with zero height

How do we decide if m widths is 1 or more? if any width within 0, n is 0

how do you quickly find the next smallest item in an array?

can you use a sorted list then make an array of indecies?

so each ordered item in the indecies array corresponds to the index of the next largest element

aight let's try it laughing crying emoji


```python
class Solution(object):
    def largestRectangleArea(self, heights):

        sorted_indecies = sorted(range(len(heights)), key=lambda i:heights[i]) # time complexity of this operation is 
        # o (n log n)

        # now the first element of sorted_indecies is the index of the smallest element of heights

        self.largest = 0
        def dfs(left_index, right_index, smallest):
            # we are going to find the smallest element within the arr then we can decide the area of this section to be ( right_index - left_index ) * smallest_within then the elements to the right and left (or more sections than that) will be passed to the next iteration
            section_area = ( right_index - left_index ) * smallest
            if section_area > self.largest:
                self.largest = section_area

            breaks = []
            for i in range(len(sorted_indecies)):
                if heights[sorted_indecies[i]] > smallest and sorted_indecies[i] in range(left_index + 1, right_index):
                    breaks.append(sorted_indecies[i])
            breaks.sort()
            for i in range(len(breaks)):
                if i == 0:
                    dfs(left_index, breaks[i] - 1, heights[left_index])
                elif i == len(breaks):
                    dfs(breaks[i]+1, right_index, heights[breaks[i]+1])
                else:
                    dfs(breaks[i] + 1, breaks[i+1] - 1, heights[breaks[i + 1]])


        dfs(0, len(heights), 0)
        return self.largest
```

Last try: we watched a video where the guy made a monotonic stack of tuples ordered by their index and then found the area by sweeping out from that index and presumably did the same thing on the way back?? brooo

neetcode solution: 

```py
def largestRectangleArea(self, heights):
    maxArea = 0
    stack = [] # stack of tuples -> (index, height)

    for i, h in enumerate(heights): # for every index and height in the list of heights:
        start = i
        while stack and stack[-1][1] > h:
            index, height = stack.pop()
            maxArea = max(maxArea, height * (i - index))
            start = index
        stack.append((start, h))
    
    for i, h in stack:
        maxArea = max(maxArea, h * (len(heights) - i))

    return maxArea
```

