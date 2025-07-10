1. Take notes on the problem

Given N pairs of parentheses, write a function to generate all combinations of well formed parentheses

The problem requires only one input N, and outputs a list of strings.

The length of each string for any n = n * 2

n left parentheses, n right parentheses

"well-formed" => follows the rules of opening and closing parentheses

-----

2. Theorize on how problem is solved 

Define well formed parentheses:
Generate the parentheses from left to right, the number of right parentheses must never be greater than the number of left parentheses
the number of left parentheses must never exceed n

therefore you want to solve by backtracking or dfs, generating every solution but as you generate it if it violates any one of the rules you can immediately eliminate it

-----

3. Learn optimal solution

```python
def generate_parentheses(n): 
    stack = []
    res = []

    def backtrack(openN, closedN):
        if openN == closedN == n:
            res.append("".join(stack))
            return # base case => complete sequence

        if openN < n:
            stack.append("(")
            backtrack(openN+1, closedN)
            stack.pop()

        if closedN < openN:
            stack.append(")")
            backtrack(openN, closedN+1)
            stack.pop()

        backtrack(0,0)
        return res
```

-----

4. Take notes on what you didn't know, mark reading as todo if necessary

what I didn't get at first is that its literally dfs

But we are using a few tricks here that confused me:

- we are using a global 'res' variable that contains a list of all the possible solutions

- when we encounter a complete solution with no error, we write from the stack to the res arr

- the ordering of the conditions matters because it feels like not only could we write after the soln has been verified then modified but it also feels like the ordering of the parentheses could create a race condition? What would happen if we switched the openN check with the closedN check?

- the function call stack interplays with the actual stack of parentheses in a way that I don't like or fully understand

other than that I kinda get it but I doubt that I would be able to recreate it.

Let's try to recreate it from memory (not looking)

```python


def generate_parentheses_backtracking(n):

    res = [] # we will populate this with the complete solutions
    stack = [] # we will use this arr to generate solutions one at a time

    def backtrack(openN, closedN):
        # openN, the number of open parentheses, closedN, the number of closed parentheses

        # base case: when the number of open and closed equal the number of pairs
        if openN == closedN == n:
            # then on the stack array must be a well formed arr of parens
            # arr.pop returns and deletes item at the end of the array?
            res.append(stack.pop())

        # check if we can add another open one
        if openN < n:
            stack.append("(")

```

Okay so basically what I forgot is the order which you do the operations. it's: 
- Append L or R paren
- Call backtrack
(if base case join stack together and add to res)
- pop stack

Then all you have to do is call backtrack with zero 

it's backtracking / dfs because when you make it past the base case, both possible paths will be taken. Also only the paths with the correct sequence will be taken.