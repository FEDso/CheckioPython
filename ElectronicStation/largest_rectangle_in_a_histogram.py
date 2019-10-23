"""
 "Your power to choose can never be taken from you.
It can be neglected and it can be ignored.
But if used, it can make all the difference."
― Steve Goodier

You have a histogram. Try to find size of the biggest rectangle you can build out of the histogram bars.

Input: List of all rectangles heights in histogram

Output: Area of the biggest rectangle

Example:

largest_histogram([5]) == 5

largest_histogram([5, 3]) == 6

largest_histogram([1, 1, 4, 1]) == 4

largest_histogram([1, 1, 3, 1]) == 4

largest_histogram([2, 1, 4, 5, 1, 3, 3]) == 8

How it is used: There is no way the solution you come up with will be any useful in a real life. Just have some fun here.

Precondition:
0 < len(data) < 1000
"""

def largest_histogram(histogram):
    if len(histogram) == 1:
        return histogram[0]
    m = max(histogram)
    rectangle = histogram[0]
    heights_last = [0 for _ in range(m)]
    for height in histogram:
        for i in range(m):
            if i < height:
                heights_last[i] += 1
                if (i+1)*heights_last[i] > rectangle:
                    rectangle = (i+1)*heights_last[i]
            else:
                heights_last[i] = 0
    return rectangle



if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert largest_histogram([5]) == 5, "one is always the biggest"
    assert largest_histogram([5, 3]) == 6, "two are smallest X 2"
    assert largest_histogram([1, 1, 4, 1]) == 4, "vertical"
    assert largest_histogram([1, 1, 3, 1]) == 4, "horizontal"
    assert largest_histogram([2, 1, 4, 5, 1, 3, 3]) == 8, "complex"
    print("Done! Go check it!")
    
