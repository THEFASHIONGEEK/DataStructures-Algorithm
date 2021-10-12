    def maximumSumSubarray (K,Arr,N):
        j ,i = 0,0
        subarr_sum = 0
        max_sum = 0
        while (j < N):
            subarr_sum += Arr[j]
            
            if (j-i+1 < K):
                j+=1
            
            elif (j-i+1 == K):
                max_sum = max(max_sum,subarr_sum)
                subarr_sum -= Arr[i]
                i+=1
                j+=1
        
        return max_sum