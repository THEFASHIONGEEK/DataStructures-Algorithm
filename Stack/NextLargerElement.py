def nextLargerElement(arr,n):
    #code here
    stack = []
    res = []
    for i in range(n-1,-1,-1):
        if  len(stack)==0:
            res.append(-1)
        elif stack[-1] > arr[i]:
            res.append(stack[-1])
        elif stack[-1]<=arr[i]:
            while (len(stack)>0 and stack[-1]<=arr[i]):
                stack.pop()
            if  len(stack)==0:
                res.append(-1)
            elif stack[-1] > arr[i]:
                 res.append(stack[-1])
        stack.append(arr[i])
    res.reverse()
    return res
