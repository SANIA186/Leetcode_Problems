class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        a= set()
        while n!=1 :
            if n in a:
                 return False
            a.add(n)
            n=sum(int(d)*int(d)for d in str(n) )
        return True
