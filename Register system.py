n = int(input())
names = {}

for i in range(n):
    name = input()
    
    if name not in names:
        names[name] = 1
        print("OK")
    else:
        print(name + str(names[name]))
        names[name] += 1
