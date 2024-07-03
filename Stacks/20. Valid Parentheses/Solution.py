
class Solution(object):
    """
    READING THROUGH PROBLEM:
    []() Valid
    [()] Valid
    ([)] NOT VALID
    What makes it not valid:
        open brackets must be closed in the correct order
        therefore
    """
    def isValid(self, s):
        bracket_stack = []
        
        for char in s:
            if char in ["[", "(", "{"]:
                bracket_stack.append(char)
            elif char in ["]", ")", "}"] and len(bracket_stack) > 0:
                open_bracket = bracket_stack.pop()
                if char == "]":
                    if open_bracket != "[":
                        return False
                if char == "}":
                    if open_bracket != "{":
                        return False
                if char == ")":
                    if open_bracket != "(":
                        return False
            else:
                return False
            
        if len(bracket_stack) != 0:
            return False
        return True