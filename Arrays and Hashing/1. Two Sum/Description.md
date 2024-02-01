Problem: 

> Given an array of integers `nums` and an integer `target`, return *indices of the two numbers such that they add up to `target`*.
> 
> 
> You may assume that each input would have ***exactly* one solution**, and you may not use the *same* element twice.
> 
> You can return the answer in any order.
> 

My Solution:
Time complexity: O(n^2) 

because if you add one more number, then you will have the same time as one less, but you have to compare each item one more time. Even though you are only comparing the numbers after the one you are checking, adding one will cause n more checks

**Better Solution: Hash Map**

A hash map is good because a hash map has a “search” function that when given a key, it will find the value of that key in O(n) time using O(n) memory.

you can implement hash map in python using dictionaries

1. Finding the pair can be made easy using the fact that hash map has a search function, and you can use this to find the complement of the number that you are currently checking
2. Create Dictionary (hash map)
3. for each number in the list, check if the complement is in the dictionary. if it is, return the value stored by the complement, which is the index of the complementing number, and the value of run of the loop
4. if it isn’t, add the pair to the dictionary, with the key being the number and the value being its index.