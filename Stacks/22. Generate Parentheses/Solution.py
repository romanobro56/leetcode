class Solution:
    def generateParenthesis(self, n):
        # only add open paren if open < n
        # only add closin paren if close < open < n
        # valid iff open == close == n

        stack = []
        res = []
        def backtrack(openN, closedN):
            res.append("".join(stack))