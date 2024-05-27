class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanumeric_arr = [i.lower() for i in s if i.isalnum()]
        a = 0
        b = len(alphanumeric_arr) - 1
        while (a < b):
            if alphanumeric_arr[a] != alphanumeric_arr[b]:
                return False
            a+=1
            b-=1
        return True