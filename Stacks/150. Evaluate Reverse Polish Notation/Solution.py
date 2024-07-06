class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        READING THROUGH THE PROBLEM:
        addition divison subtraction multiplication
        its just a stack where the two most recent ints are used in the operation
        add numbers to the stack and when an operation occurs pop the two most recent 
        numbers and push the result
        """
        num_stack = []
        for char in tokens:
            if char == "+":
                num_stack.append(num_stack.pop() + num_stack.pop())
            elif char == "-":
                b,a = num_stack.pop(), num_stack.pop()
                num_stack.append(a - b)
            elif char == "/":
                b,a = num_stack.pop(), num_stack.pop()
                result = abs(a) // abs(b)
                if (a < 0) ^ (b < 0):  # Check if the result should be negative
                    result = -result
                num_stack.append(result)
            elif char == "*":
                num_stack.append(num_stack.pop()* num_stack.pop())
            else:
                num_stack.append(int(char))

        return num_stack[0]