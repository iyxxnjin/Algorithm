N, K = map(int, input().split())
temp = list(map(int, input().split()))

range_sum = sum(temp[:K])
max_sum = range_sum

for i in range(K, N):
    range_sum += temp[i] - temp[i-K]
    max_sum = max(max_sum, range_sum)

print(max_sum)
        
    

