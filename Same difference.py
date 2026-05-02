t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    freq = {}
    count = 0
    
    for i in range(n):
        val = arr[i] - i
        if val in freq:
            count += freq[val]
            freq[val] += 1
        else:
            freq[val] = 1
    
    print(count)
