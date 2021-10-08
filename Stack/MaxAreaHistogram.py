def SmalltoRight(arr,n):
    right = []
    stack = []
    
    for i in range(n-1,-1,-1):
        if len(stack) == 0:
            right.append(n)
        elif stack[-1][0] < arr[i]:
            right.append(stack[-1][1])
        elif len(stack)>0 and stack[-1][0] >= arr[i]:
            while(len(stack)>0 and stack[-1][0] >= arr[i] ):
                stack.pop()
            if len(stack) == 0:
                right.append(n)
            else:
                right.append(stack[-1][1])
        stack.append([arr[i],i])
        
    right.reverse()
        
    return right


def SmalltoLeft(arr,n):
    left = []
    stack = []
    
    for i in range(n):
        if len(stack) == 0:
            left.append(-1)
        elif stack[-1][0] < arr[i]:
            left.append(stack[-1][1])
        elif stack[-1][0] >= arr[i]:
            while(len(stack)>0 and stack[-1][0] >= arr[i] ):
                stack.pop()
            if len(stack) == 0:
                left.append(-1)
            else:
                left.append(stack[-1][1])
        stack.append([arr[i],i])
    
    return left
    
    
def getMaxArea(histogram):
    #code here
    n = len(histogram)
    
    right = SmalltoRight(histogram,n)
    # print(right)
    left  = SmalltoLeft(histogram,n)
    # print(left)
    width = []
    area  = []
    for i in range(n):
        width.append(right[i]-left[i]-1)
    # print(width)
    for i in range(n):
        area.append(histogram[i]*width[i])
    return max(area)
        
    
