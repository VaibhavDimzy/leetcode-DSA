class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        size=len(nums)
        missing_lst=[]
        for i in range(size+1):
            missing_lst.append(0)

        final=[]
        # while(i<=size):
        for i in nums:
            missing_lst[i]=1
        
        for i in range(1,len(missing_lst)):
            if missing_lst[i]==0:
                final.append(i)
        return final
        