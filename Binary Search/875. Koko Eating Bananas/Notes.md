For starters, I have definitely solved this problem before albeit shittily.

I read the solution, fully understood and digested it before writing my own solution which makes the most sense to me and fits into my mental framework for how binary search problems work.

This I am proud of. Not just for doing it but rather figuring out the way which will help me learn algorithms the best.

This follows leetcode advice I have recieved which states that you should split the problems into ones you want to learn the solution from and others you want to practice solving (like ml training data).

About the problem specifically, It was good that I asked chat jibidy to first tell me why it wasn't solvable mathematically, then from there I asked how would an experienced engineer / algos expert know that it wasn't solvable mathematically, then I asked to put that in "swe intern terms" which was intuitive but it wasn't watered down. 

At the heart of the problem is a core formula, sum(ceil(pile * k)) < H. This is how we know the formula isn't one to be computed but rather k is a solution space you binary search over.

I think that writing down the core math underlying the problem you are solving is a good starting point, but you may have to mentally detach that process from trying to derive the solution from the process to first be able to understand where to go.