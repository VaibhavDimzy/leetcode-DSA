class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        #APPROACH 1 BRUTE FORCE
        
        # for i in range(len(nums)):
        #     sum_from_start=0
        #     sum_from_end=0
        #     for left in range(0,i):
        #         sum_from_start+=nums[left]

        #     for right in range(i+1,len(nums)):
        #         sum_from_end+=nums[right]

            
        #     if (sum_from_start==sum_from_end):
        #         return i

        # return -1

        #APPROACH 2
        sum=0
        left_sum=0
        for i in nums:
            sum=sum+i
        print(sum)


        for i in range(len(nums)):
            print(left_sum,sum)
            if left_sum == (sum-nums[i]):
                return i
            else:
                left_sum +=nums[i]
                sum -=nums[i]
        
        return -1
        