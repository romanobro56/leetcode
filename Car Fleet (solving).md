There are n cars at given miles away from the startin mile 0, traveling to reach the mile target.

you are given tow integer array position and speed, both of length n, where position[i] is the stratign mile of the ith car and speed[i] is the speed of the ith car in miles per hour

A car cannot pass another car but it can catch up and then travel next to it at the speed of the slower car

A car fleet is a car or cars driving next to each other The speed of the car fleet is the minimum speed of any car in the fleet

if i car catches up to a car fleet at the mile target, it will still be considered as part of the car fleet.

return the number of car fleets that will arrive at the destination


-----
Notes:

Question: if Car A just crosses the finish line and is going 10 miles per hour, and they are at the finish line mile (let's say 10), and Car b starts 11 miles away but goes 11 miles per hour does that mean they join as a fleet or no? the question statement leads me to believe yes

Why ts so mathy yuck

So we can just have an array of each of the starting positions and then divide it by the speed to get how long it takes the car to get to the finish line and then every car that is bottlenecked by a car ahead of it will be part of the fleet?

"the speed of the car fleet is the minimum speed of any car in the fleet" makes me think it's not that simple but where do the stack come into play

Im trying to think of why my solution wouldn't work but i don't see why so i'll try it

Ahh wait - a car is going it's own speed until it reaches the car fleet - ???

```python

def count_fleets(target, position, speed):
    distances = [target - pos for pos in position]
    time_to_finish = []
    for i, distance in enumerate(distances):
        time_to_finish[i] = distance / speed[i]

    # now we should have an array of times and then we will pop 
    # all the speeds that are slower than one ahead of it and count that as a car fleet

    slowest_of_pack = time_to_finish[-1]
    fleets = 0

    for time in reverse(time_to_finish):
        if time > slowest_of_pack:
            fleets += 1
            slowest_of_pack = time
    
    return fleets
```

Asking chat for hint - I thought the distances array was already sorted but it wasn't

if it was sorted then the logic would be sound

cars = sorted(zip(position,speed), reverse=True)

if you didn't know zip it would look something like this

```python
cars = []
for i in range(len(position)):
    cars.append(position[i], speed[i])

cars.sort(reverse=True)
```