a =str(input())
first = a[:a.find('h')] 
reverse = a[a.find('h'):a.rfind('h') + 1]
last = a[a.rfind('h') + 1:]
final = first + reverse[::-1] + last
print(final)  