a = str(input())
b = a.find('f')
c = a.rfind('f')
if b == c:
    print(b)
else:
    print(b, c) 