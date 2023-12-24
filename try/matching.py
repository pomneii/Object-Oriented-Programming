
# matching 

"""
    Hi, Hello
    Pink, kiki
    Hi Pink, Hi kiki, Hello Pink, Hello kiki
"""

greeting = ["Hi", "Hello", "What's up", "Bye", "Goodbye"]
people = ["Pink", "kiki", "kuku", "bobo"]
result = []

# normal
for x in greeting :
    for y in people :
        result.append(x + y)
print(result)

# easy way to write
greeting = ["Hi", "Hello", "What's up", "Bye", "Goodbye"]
people = ["Pink", "kiki", "kuku", "bobo"]
result = []

result = [i + j for i in greeting for j in people]
print(result)