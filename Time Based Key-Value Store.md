1. Take notes on the problem

Class based solution with methods and data

Timestamps are strictly increasing

Key value pairs stored and 
-----
2. Theorize on how problem is solved 
-----
3. Try solving

```py
class TimeMap(object):

    def __init__(self):
        self.keys = {}

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        if key not in self.keys:
            self.keys[key] = [(timestamp, value)]
        else:
            self.keys[key].append((timestamp, value))
        

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        if key not in self.keys:
            return ""

        timed_values = self.keys[key]
        l, r = 0, len(timed_values) - 1

        while l <= r:
            mid = (l + r) // 2
            if timed_values[mid][0] == timestamp:
                return timed_values[mid][1]
            if timed_values[mid][0] < timestamp:
                l = mid + 1
            else:
                r = mid - 1
        if timed_values[l][0] <= timestamp:
            return timed_values[l][1]
        else:
            return ""
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
```
3.5 Give it 30 minutes of genuinely trying past the point you think theres 0 percent chance you will solve it 

OR 

Congrats!, continue to step 4
-----
4. Take notes on what you didn't know, mark reading as todo if necessary

Let's go it workde

I just don't know why the original binary search I wrote didn't work 

I traced it but didn't understand it at a fundamental level

Let's ask chat to compare the two submissions
-----
5. Metanotes