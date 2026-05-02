from collections import defaultdict
t = int(input())
dict1 = defaultdict(int)
for i in range(t):
    word = input()
    dict1[word]+=1
_max = 0
word = ""
for i in dict1:
    if dict1[i]>_max:
        _max = dict1[i]
        word = i
print(word)
