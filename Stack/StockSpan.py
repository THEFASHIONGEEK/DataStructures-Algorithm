def stockspan(arr,n):
    span = []
    stack = []
    for i in range(n):
        if len(stack) == 0:
            span.append(-1)
        elif stack[-1][0]>arr[i]:
            span.append(stack[-1][1])
        elif stack[-1][0]<=arr[i]:
            count = 1
            while(len(stack) > 0 and stack[-1][0]<=arr[i]):
                stack.pop()
            if len(stack) == 0:
                span.append(-1)
            elif stack[-1][0]>arr[i]:
                span.append(stack[-1][1])
            
        stack.append([arr[i],i])
    for i in range(n):
        span[i] = i - span[i]
    return span
t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    res = stockspan(arr,n)
    for i in range(n):
        print(res[i],end = " ")
    print()
            