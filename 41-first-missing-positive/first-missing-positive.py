class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        size=len(nums)
        missing_lst=[]
        for i in range(size+1):
            missing_lst.append(0)

        for i in nums:
            if i <= size and i>0:
                missing_lst[i]=1
        
        for i in range(1,len(missing_lst)):
            if missing_lst[i]==0:
                return i
        return size+1
       

        