1. Take notes on the problem

Understanding the problem: The array is sorted, and it may or may not be rotated by x. "rotated" means that all of the values are left shifted x times. The resulting array is still sorted but the 'end' of the array is somewhere in the middle of the array.

Must be in O(log n) time

Must return the index of the "target" or -1 if it is not in the array

The array is sorted ascending

The array has distinct values

-----
2. Theorize on how problem is solved

Theory 1: brute force

Enumerate through the array and for each value if it is the target value then you can return that index. If you get to the end of the array and it's not there you return -1

Theory 2: better soln.

A regular binary search is O(log n) so if you can first search for the smallest by tweaking the binary search algorithm then you can take note of the shifts then you can perform a normal binary search operation on the array but every time you calculate indecies you shift it to get the original unshifted array. O(log n) + O(log n) = O(log n)

Problem: how are you gonna perform the initial binary search if it's not sorted?

I bet you could use the directionality of the numbers

But if you could do that why don't you use that to just solve the problem in one go?

If number right of our number is greater, and the target is less, search for it on the left

but then it could be on the right

So what you have to do is make the array on a continum somehow

I definitely think you will have to use the mod operation somewhere in the solution

But the 'make the array on a continum' theory is conflicting with the need to know where the greatest is still in order to perform a binary search

If you get plopped down in an ordinary binary search but you don't know where you are does it still work? Yes it must but no it wont lol because you have to account for the numbers you might not ever see

So what you should do in that case is make sure you get visibility of all the numbers 

But in this problem we can do that by doubling the size of the first search surface area

If you had the numbers on a circle would you be able to do a binary search 

*imagining*

I think i got it 

It only matters about the first operation

If you do the first/second operation and the number is greater or less than the whole range you covered in the first operation then you have to continue doing that otherwise **it's just a regular binary search**

This gets more complicated but I think that might be the way

Anyhow I decided this problem would be a 'learn the solution' problem not a 'do the problem' problem so let's move on

-----
3. Learn optimal solution
    3.5 Write out solution

```py

class Solution:
    def search(self, nums, target):
        l,r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            
            # now find if we are in the left sorted portion of the array or the right sorted portion of the array
            if nums[l] < nums[mid]:
                if target > nums[mid]:
                    l = mid + 1
                elif target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1

        return -1

```
-----
4. Take notes on what you didn't know, mark reading as todo if necessary

What I didn't know wasn't too much, I just ran a circle around the real answer

to reiterate, the base binary search:

```py
l, r = 0, len(arr) -1
while l <= r:
    mid = (l + r) // 2
    if arr[mid] == target:
        return target
    elif arr[mid] < target:
        l = mid + 1
    else:
        r = mid - 1
```

-----
5. Metanotes

I was close to solving it because I believe that solution method crossed my mind once but I thought there was a 'smart' way to do it... what do we call this? Casework? Just solving each of the cases when you get to a point in the problem when you have a few possible ways things could go. But its built on top of an algorithm. So it's not brute force