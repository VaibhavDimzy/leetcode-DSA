class Solution:
    def missingNumber(self, nums: List[int]) -> int:


        i=0
        while(i<len(nums)):
            if i!=nums[i] and nums[i]<len(nums):
                j=nums[i]
                nums[i],nums[j]=nums[j],nums[i]
            else:
                i+=1

        for a in range(len(nums)):
            if a != nums[a]:
                return a

        return len(nums)



        #APPROACH 3
        # total=0

        # for i in nums:
        #     # print(total)
        #     total = total^i
        # print(total)
        # for i in range(len(nums)+1):
        #     total=total^i

        # return total
        #APPROACH 2
        # number={}
        # for i in nums:
        #     if i in number:
        #         number[i]+=1
        #     else:
        #         number[i]=1
        


        # for i in range(len(nums)):
        #     if i not in number:
        #         return i

        # return len(nums)
                
        #APPROACH 1
        # for i in range(len(new_arr)):
        #     if i != new_arr[i]:
        #         return i

        # return len(new_arr)

        