I solved this problem in theory very very easily

the real problem was why the division wasn't working
basically the divison should truncate TOWARDS 0
that means you need to use the absolute value of both integers to perform integer divison on them
this is because if say -7 / 4 should truncate towards zero which is towards -1
But integer divison -7 / 4 = -2 because at least python integer divison truncates down regardless
So after using the absolute value to make sure that it truncates towards zero always,
you have to add a check to make the result negative if one of the inputs was negative

But I didn't think of that, chatgpt did. You could do if/else but what chatgpt did was even smarter
python operator  ^ is XOR
XOR => true if one is true and the other is false
therefore if input 1 is negative XOR input 2 is negative, the result should be negative
(a < 0) ^ (b < 0)

also had to make sure that the order that you pop them is the order that you want to do the operation on them.