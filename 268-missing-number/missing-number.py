class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        number={}
        for i in nums:
            if i in number:
                number[i]+=1
            else:
                number[i]=1
        


        for i in range(len(nums)):
            if i not in number:
                return i

        return len(nums)
                

        # for i in range(len(new_arr)):
        #     if i != new_arr[i]:
        #         return i

        # return len(new_arr)

        