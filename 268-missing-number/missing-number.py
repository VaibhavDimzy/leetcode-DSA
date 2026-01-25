class Solution:
    def missingNumber(self, nums: List[int]) -> int:

    
        new_arr = sorted(nums)

        for i in range(len(new_arr)):
            if i != new_arr[i]:
                return i

        return len(new_arr)

        