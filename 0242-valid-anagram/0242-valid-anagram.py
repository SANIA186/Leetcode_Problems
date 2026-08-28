class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # return sorted(t)== sorted(s)

        

        if len(s) != len(t):
            return False

        hashmap = {}

        
        for ch in s:

            hashmap[ch] = hashmap.get(ch, 0) + 1

        
        for ch in t:

            if ch not in hashmap:
                return False

            hashmap[ch] -= 1

            if hashmap[ch] < 0:
                return False

        return True