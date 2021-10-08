class Solution:
    def trappingWater(self, arr,n):
        left_count = [0]*n
        left_count[0] =arr[0]
        right_count = [0]*n
        water = 0
        for i in range(1,n):
            left_count[i] = max(arr[i],left_count[i-1])
        right_count[n-1] = arr[n-1]
        for i in range(n-2,-1,-1):
            right_count[i] = max(arr[i],right_count[i+1])
            
        for i in range(0,n):
            water += min (right_count[i],left_count[i])-arr[i]
        return water