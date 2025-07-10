(learning solution)
I believe I would easily determine this is a stack problem without knowing the category: when each entry needs to "close" given that it "opens", a stack is best fit to track that behavior

Brute force: generate every possible pair of parentheses, use a stack to check if there's a "leading" close or a "trailing" open

Wait, is that just the solution?

Let me try it

How do you generate every possible combination?

How many combinations are there? Then you have a nested loop where you take the mod to determine if it's open or close

1 pair: 2 possible
2 pair:
`((((`
`)(((`
`()((`
`))((`
`())(`
`)))(`
`(()(`
`)()(`

Ok bruh I really can't come up with the 'natural' way of generating the parentheses. 

Ok what if you limit it to only the options that have equal amount of open and closed?

`(())`
`)()(` => this order was chosen because you switched the first option to the other option and then filled the last item with the only paren left
`())(` => this order was chosen because the second place is switched and the rest is filled with first, the original sequence then what's left
`))((`=> last possible option of the first two, is this the last possible option?
No

is 2^n = number of possible paren combinations

no

uhh

wait i was supposed to be learning the solution not solving it

ok so far: its backtracking but stack so you just make sure the number of close never exceeds the number of open while you are constructing it and also the number of opens is limited to n

bro i don't know backtracking thats below stacks on the roadmap how was i supposed to formulate this solution anyway

ok so wtf 

navdeep you failed me
