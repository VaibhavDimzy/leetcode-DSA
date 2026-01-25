class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        sum=0
        left_sum=0
        for i in nums:
            sum=sum+i
        # print(sum)


        for i in range(len(nums)):
            # print(left_sum,sum)
            if left_sum == (sum-nums[i]):
                return i
            else:
                left_sum +=nums[i]
                sum -=nums[i]
        
        return -1
        