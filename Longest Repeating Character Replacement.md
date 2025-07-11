1. Take notes on the problem

You have to find the longest repeating substring of a given string where you can change up to K characters to any letter within that substring

The longest substring could be comprised of any possible characters

-----
2. Theorize on how problem is solved 

Similar to the stock problem, you keep track of the left (first instance of the repeating) character

As you keep track, the longest substring will get longer. And when it gets longer, that means you have less possible changes to make, and when you have less possible changes to make, you can look at less characters as you progress through the substring

This is what I believe is the optimal solution to prevent o(n^2) because instead of a continuous, orderd problem space (numbers), you have a discrete unordered problem set (letters)

So if you solved it without decreasing your tolerance for missing letters you would have to look at each letter in sequence and potentially compare it to the rest of the string

a. Look at first letter, and see how big of a repeating substring you can make

let's say you can make a 7 letter repeating substring with k = 2

Now you know if you encounter two non repeats before reaching 7 you can move to the next letter

then you make a 9 letter repeat with only two 

then if you encounter two letters before you reach 9 then you can skip
-----
3. Learn optimal solution

Ok so basicaly what the fuck

Navdeep solution, telephone version

Within the window you have a hash map that represents all of the letters and their frequencies within the window

You can increment the right pointer when the following condition is true

    3.5 Write out solution


```py
class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # char_arr = list(s) - if necessary
        l, r = 0, 0
        longest = 0
        char_counts = {}
        while r < len(s) - 1:
            if len(char_counts) == 0:
                r += 1
                break
            max_count = 0
            for key in char_counts:
                max_count = max(max_count, char_counts[key])
            # now max_count represents the number of the most repeating characters in the window
            # we don't yet know if we should be adding the next character from the right or incrementing the left, we should do that now
            if (r - l + 1) < (max_count + k):
                # we have more room to add the next character
                r += 1
                if r < len(s):  # guard against index error
                    char_counts[s[r]] = char_counts.get(s[r], 0) + 1
                    longest = max(char_counts[s[r]] + k, longest)
            else:
                char_counts[s[l]] -= 1
                l += 1
            
            # (r - l) + 1 - the number of chars in the window

        return longest
        
```

okay this was typed out when my data wasn't working on the train so now we will actually copy it from the video and compare the two

```py
class Solution:
    def characterReplacement(self, s, k):
        count = {}
        res = 0

        l = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0) # dict get => create or replace kinda thing

            while (r - l + 1) - max(count.values()) > k: 
                # okay so I got the guards right
                # count.values => array of values?
                # taking the max of that is O(26)
                # (because we know there is max 26 values, then do this for every entry, then soln is O(26n))
                count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)
        return res
```

-----
4. Take notes on what you didn't know, mark reading as todo if necessary

I didn't think that we would use 'nested' data structures in a leetcode medium but here we are
-----
5. Metanotes