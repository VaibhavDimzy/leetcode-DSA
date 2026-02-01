class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        #APPROACH 1 = pehle ek new khal list banai jisme sari values 0 de diya. then ek new loop chalaya nums mai and num[i] mai jo value hai vo value ka missing_values ke index mai jake usko 1 mark kardo. then ek loop aur chalao jisme missing_values mai jo 0 hai usko ek nye list mai save karke list return kardo.
        # size=len(nums)
        # missing_lst=[]
        # for i in range(size+1):
        #     missing_lst.append(0)

        # final=[]
        # # while(i<=size):
        # for i in nums:
        #     missing_lst[i]=1
        
        # for i in range(1,len(missing_lst)):
        #     if missing_lst[i]==0:
        #         final.append(i)
        # return final


        #APPROACH 2

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
                final.append(j+1)

        return final
        