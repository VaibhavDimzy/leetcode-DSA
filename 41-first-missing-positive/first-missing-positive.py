class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        size=len(nums)
        i=0
        final=[]
        while(i<size):
            correctIdx=nums[i]-1
            if nums[i]<1 or nums[i]>size-1 or nums[correctIdx]==nums[i]  :
                i+=1
            else:
                nums[i],nums[correctIdx]=nums[correctIdx],nums[i]
        for j in range(size):
            if j+1!=nums[j]:
                return(j+1)

        return size+1

