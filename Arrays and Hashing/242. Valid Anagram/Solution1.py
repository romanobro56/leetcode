class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
        # length of a string is obtained with the len() function and nor 
				# checks are done with a single exclamation mark
            return False

        countS, countT = {}, {}
        # curly braces define the initial values in a "dictionary" in python
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
            # this is setting the key (the character being accessed) to 
            # increase its count by one. The get function allows the entry 
						# to be created if there is one with the value of the second 
						# parameter to the function.
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False

        return True