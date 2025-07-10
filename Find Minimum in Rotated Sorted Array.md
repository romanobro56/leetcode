1. Take notes on the problem

~ Yoo this seems easy now that I did the other one! Let's go ~

Array is unique

Return the minimum element

O(log n)

Rotated n times - the array is still sorted but the 'break' (where the greatest and least num meet) could be anywhere in the array including the middle and the ends

-----
2. Theorize on how problem is solved 

We can easily access the values of the ends of the array in O(1) time. Because of this, we can always know where we are relative to the smallest number despite the array being rotated.

Here are the possible cases

Case 1: 'break' of the array is to the left of our mid pointer, and the smallest is also to the left

arr[0] is greater than mid, arr[last] is also greater than mid

=> search left

Case 2: 'break' of the array is to the right of our mid pointer, and the smallest is also to the right

arr[0] is less than mid, arr[last] is also less than mid

=> search right

Case 3: array is sorted normally

arr[0] is less than mid, arr[last] is greater than mid

=>

does this mean we can immediately return the arr[0] ? 

No because if you want to keep that logic in the loop then it breaks when you start looping

-----
3. Try solving

```py

class Solution:
    def findMin(self, nums):
        l,r = 0, len(nums) - 1

        if nums[l] < nums[r]:
            return nums[0]

        self.mid = 0
        while l <= r:
            self.mid = (l + r) // 2
            if nums[l] > nums[self.mid]:
                l = self.mid + 1
            else:
                r = self.mid - 1
        
        return nums[self.mid]

```

3.5 Give it 30 minutes of genuinely trying past the point you think theres 0 percent chance you will solve it 

Okay think about the win condition: the pointers should converge on the smallest element in the array. We will iterate geting smaller until both pointers are on the smallest number and then return that value

We always want to search towards the break => converge on the element where the element before (and every element preceding) it is larger than it

if the left pointer is greater than the mid pointer, then we know the break is between left and mid

if the right pointer is smaller than the mid pointer, then we know the break is between right and mid

```py
class Solution:
    def findMin(self, nums):
        l,r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) // 2
            if nums[l] > nums[mid] and l < mid - 1:
                r = mid - 1
            elif nums[r] < nums[mid] and r > mid + 1:
                l = mid + 1
            else:
                return min(min(nums[l], nums[mid]), nums[r])

```

bro how do you make it converge when the same logic that drives the 

last try:

```py

class Solution:
    def findMin(self, nums):
        l,r, = 0, len(nums) - 1

        if nums[l] <= nums[r]:
            return nums[l]

        while l < r:
            mid = (l + r) // 2
            if r - l <= 2 or nums[mid - 1] > nums[mid]:
                return min(nums[l], min(nums[mid], nums[r]))
            if nums[l] > nums[mid]:
                r = mid - 1
            else:
                l = mid + 1

        return - 1

```

CHAT:

```py
class Solution:
    def findMin(self, nums):
        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) // 2

            # mid in left (larger) piece → discard left half including mid
            if nums[mid] > nums[r]:
                l = mid + 1
            # mid in right (smaller) piece → keep left half including mid
            else:
                r = mid        # NOT mid - 1; we might be on the min itself

        return nums[l]

``` 
OR 

Congrats!, continue to step 4
-----
4. Take notes on what you didn't know, mark reading as todo if necessary

I got the base solution - the details were lost on me though.

-----
5. Metanotes

I should have knew it was simpler than manually doing edge cases

I should have took some more time to get a more elegant solution by using my brain? 