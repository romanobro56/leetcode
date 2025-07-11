1. Take notes on the problem

returning the length as an int

s can be really long

s includes numbers symbol and spaces

character duplicates just mean two of any of the same thing
-----
2. Theorize on how problem is solved 

I think it is quite similar to the longest repeating problem, but instead we just have a hash table. If the rightmost character - wait no that's wrong

we need a hash map where the instance of the character maps to it's index in the array - then we can update the left pointer to be after the duplicate

I think we can use enumerate because there is no condition in which we don't have to update r every iteration

I will call this version of the sliding window 'lagging left pointer' 


-----
3. Try solving
```py
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        chars = {}
        l = 0
        
        for r, char in enumerate(s):
            if l >= len(s):
                break
            elif char in chars:
                l = chars[char] + 1
                for elim_char in chars.keys():
                    if chars[elim_char] < l:
                        chars.pop(elim_char)
            else:
                chars[char] = r
                res = max(res, r - l)

        return res
```


3.5 Give it 30 minutes of genuinely trying past the point you think theres 0 percent chance you will solve it 

okay bruh after 1 submission idk what the problem is so I'm moving this over here
```py
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        chars = {}
        l = 0
        
        for r, char in enumerate(s):
            if char in chars:
                l = chars[char] + 1
                for elim_char in chars.keys():
                    if chars[elim_char] < l:
                        chars.pop(elim_char)
            else:
                chars[char] = r
                res = max(res, r - l)

        return res

```

What I was thinking is:

```py
return max(res, len(chars.keys()))
```

but really now we just shitting edge cases but we know that usually doesn't work 

MAYBE: the right line of questioning when you get an edge case is 'do we need to do this' or 'what if we do it this way?'

Let's try:

Do we need to check if l is past the shits or is there a better way?

well we never access s[l] so we don't have to worry about out of bounds

So we just don't need to do that because if you enter the case where you set l to the len of s then it won't run the next iteration because we know it is on the last character now

Still works on the first testcases, but didn't solve the single character problem

The problem is with the way we set the length, it's not always accurate to the real length of the unique substring 

Why because when the left pointer is zero, it's not the accurate counter, otherwise it is accurate.

So if you start by setting the left pointer to negative 1, it makes the initial calculations accurate because it's basically saying 'include the 0th item in the length calculation'. And that shouldn't affect later calculations because l behaves normally once it is changed

Okay let's submit! Even though only 10 percent of test cases passed initially

Yk what let's use some discussion recommended test cases instead to not tank my submission rate

"Bruh who tf sat down and wrote 987 testcases. This is sacrilegious. Go touch grass. See the world out there gang. This is not it." 

"dvdf" did not work

move 

```py 
chars[char] = r
```

to outside the if else - solves one test case but breaks another

breaking test cases all have duplicate letters in them - identify problem please romàn

okay rôman ill do that now

YAY I DID IT NO HELP IN ABOUT THE SAME AMOUNT OF TIME AS A TECHNICAL INTERVIEW !!!

Here is my final solution:

```py
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        chars = {}
        l = 0
        
        for r, char in enumerate(s):
            if char in chars:
                l = chars[char] + 1
                for elim_char in chars.keys():
                    if chars[elim_char] < l:
                        chars.pop(elim_char)
            else:
                res = max(res, 1 + r - l)
            chars[char] = r

        return res
        
```


OR 

Congrats!, continue to step 4
-----
4. Take notes on what you didn't know, mark reading as todo if necessary

What I didn't know:

dict.keys() gives you all the keys of a dict in an array form

dict.pop() deletes the key and the value in the dict when given the key

for i, item in enumerate(items)

I did understand the problem and how to solve it, because it was very similar to the last one I did just learning!
-----
5. Metanotes

I think I finally noticed the pattern. When you see your code and it encounters some edge cases, first try to see if you can do SUBTRACTIVE coding where you simplify and reduce the code to fix the problem before you try adding barriers around your code. Because we need less complexity and leetcode problems are usually solveable in very very simple terms.