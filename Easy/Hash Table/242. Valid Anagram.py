class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        ds = collections.Counter(s)
        dt = collections.Counter(t)
        
        return ds == dt
        
# sorted

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        return sorted(s) == sorted(t)
    
    