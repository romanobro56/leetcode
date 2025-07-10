1. Take notes on the problem

You have to find the longest repeating substring of a given string where you can change up to K characters to any letter within that substring

The longest substring could be comprised of any possible characters

-----
2. Theorize on how problem is solved 

Similar to the stock problem, you keep track of the left (first instance of the repeating) character

As you keep track, the longest substring will get longer. And when it gets longer, that means you have less possible changes to make, and when you have less possible changes to make, you can look at less characters as you progress through the substring

This is what I believe is the optimal solution to prevent o(n^2) because instead of a continuous, orderd problem space (numbers), you have a discrete unordered problem set (letters)

So if you solved it without decreasing your tolerance for missing letters you would have to look at each letter in sequence and potentially compare it to the rest of the string

a. Look at first letter, and see how big of a repeating substring you can make

let's say you can make a 7 letter repeating substring with k = 2

Now you know if you encounter two non repeats before reaching 7 you can move to the next letter

then you make a 9 letter repeat with only two 

then if you encounter two letters before you reach 9 then you can skip
-----
3. Learn optimal solution

Ok so basicaly what the fuck

Navdeep solution, telephone version

Within the window you have a hash map that represents all of the letters and their frequencies within the window

You can increment the right pointer when the following condition is true

    3.5 Write out solution



-----
4. Take notes on what you didn't know, mark reading as todo if necessary
-----
5. Metanotes