Check if a string is a vaild anagram of another string. An anagram is a word that is made up of the same characters in another, with the same quantity of each character.

Solution 1: use 2 hashmaps that have the keys as the characters, and the amount of occurrences as the values. Then you can compare the occurences of each character and if they are all the same, then the words are anagrams of each other.

you want to make sure that they are the same length first to be sure that there is no extra characters in one string

- time complexity O(s + t): you are looping over each of the strings
- memory complexity: O(s+t): you are building two hashmaps containing the contents of the strings

Solution 2: sort the strings. If they are the same, then they are anagrams.