
# find and count in list

message = ["aa", "aab", "cba", "cca", "bab"]
result = []

for item in message :
    result.append(item.count("a"))
print(result)