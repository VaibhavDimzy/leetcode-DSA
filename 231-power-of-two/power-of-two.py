class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        count=0
        if n<=0:
            return False
        return ((n & (n-1))==0)
        # elif n==1:
        #     return True
    
        # while (n>1):
        #     rem=n%2
        #     if (rem !=0):
        #         return False
        #     n=n//2
        # while(n!=0):
        #     r=n%2
        #     if r==1:
        #         count+=1
        #     n=n//2
        # if count==1:
        #     return True
        # else:
        #     return False

        