class Solution:
    def isPalindrome(self, s):
        a = 0
        b = len(s) - 1
        while (b > a):
            while ( a < b and not self.isAlphanumeric(s[a])):
                a += 1
            while ( b > a and not self.isAlphanumeric(s[b])):
                b -= 1
            if (lower(s[a]) != lower(s[b])):
                return False
            b -= 1
            a += 1
        return True
            
    def isAlphanumeric(self, s):
        num = ord(s)
        if num > 122:
            return False
        if num < 48:
            return False
        if num < 58:
            return True
        if num < 65: 
            return False
        if num < 91:
            return True
        if num > 96:
            return True
        return False