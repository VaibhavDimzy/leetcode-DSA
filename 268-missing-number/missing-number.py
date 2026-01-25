class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        #APPROACH 3
        total=0

        for i in nums:
            print(total)
            total = total^i
        print(total)
        for i in range(len(nums)+1):
            total=total^i

        return total
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

        