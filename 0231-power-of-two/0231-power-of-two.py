class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        #using AND operator
        # return n> 0 and (n & (n-1)) == 0 

        # using XOR operator
        return n > 0 and (n ^ (n-1)) == 2*n-1
        