import heapq
from collections import Counter
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        counts = Counter(s)
        
        max_heap = [(-freq, char) for char, freq in counts.items()]
        heapq.heapify(max_heap)
        
        result = []
        while max_heap:
            neg_freq, char = heapq.heappop(max_heap)
            result.append(char * (-neg_freq))
            
        return "".join(result)