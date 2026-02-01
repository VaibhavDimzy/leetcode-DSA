class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        size=len(nums)
        i=0
        final=[]
        while(i<size):
            correctIdx=nums[i]-1
            if nums[correctIdx]==nums[i]:
                i+=1
            else:
                nums[i],nums[correctIdx]=nums[correctIdx],nums[i]
        for j in range(size):
            if j+1!=nums[j]:
                final.append(nums[j])

        return final
        
