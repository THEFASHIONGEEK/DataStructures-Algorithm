def findPeakElement(nums: List[int]) -> int:
    start = 0
    end = len(nums) -1
    size = len(nums) - 1
    
    if start == end :
        return start
    
    while start <= end :
        
        mid = start + (end-start)//2
        
        if mid > 0 and mid < size:
            if nums[mid]> nums[mid+1] and nums[mid] > nums[mid-1]:
                return mid
            elif nums[mid] < nums[mid+1]:
                start = mid+1
            else:
                end =mid-1
        elif mid == 0:
            if nums[0] > nums[1]:
                return 0
            return 1
        else:
            if nums[size]>nums[size-1]:
                return size
            return size-1