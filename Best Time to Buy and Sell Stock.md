1. Take notes on the problem

best time to buy and sell stock:

return the maximum profit (indecies do not have to be tracked here, just profit)

the buy date must be before the sell date (does this really matter because it's just the difference of two dates? answer yes because if a stock is decreasing you can't buy in the future and sell in the past and vice versa)

because of this we can know that the pointers are only moving right
-----
2. Theorize on how problem is solved 

just because a day has the lowest possible price doesn't mean that it's the buy date

the buy date should move forward as long as it's decreasing and the sell date should move forward as long as it's increasing
-----
3. Try solving

3.5 Give it 30 minutes of genuinely trying past the point you think theres 0 percent chance you will solve it 

```py
class Solution:
    def maxProfit(self, prices):
        # sliding window - we want to constrict the search area
        # once we have a 'smallest' day we want to find the largest day after the smallest day
        # we know that once we have a small day the only reason we would want to move the left pointer
        # is if there is a smaller smallest day after
        # and in that case we have to compare the difference of the new smallest and the largest that
        # must come after that to the previous smallest and the largest including up to the previous smallest
        # How about we put the right pointer at the end? Then the mechanics of both pointers work the same
        # except that makes it harder to keep track of where to go next
        # to solve I understand it now we gotta 


        # Okay I got it - we are mostly going to use the right pointer to inform our decision to update both pointers 
        # We only have to move the left pointer to the right when we encounter a new smallest number, and if 
        # there is a new highest after moving the right that is no problem because we know it's at the lowest so far. 
        # This accounts for the case where the highest is before the lowest 

        l, r = 0, 1
        greatest_profit = 0
        while r < len(prices):
            greatest_profit = max(greatest_profit, prices[l] - prices[r])
            elif prices[r] < prices[l]:
                l = r
            r += 1

        return greatest_profit
```

OR 

Congrats!, continue to step 4

LETS FReaking go
-----
4. Take notes on what you didn't know, mark reading as todo if necessary

It did take me watching navdeep's explanation of the problem in order to solve it correctly.

I don't think it was that I didn't know anything, I had a solid grasp of two pointers, sliding window and the difference between the two

I couldn't create the proper way to solve the problem from my own head
-----
5. Metanotes

I do think that visualizing the problem with the most accurate visualization you can get to the problem is 
probably the best way to get creative with the solution