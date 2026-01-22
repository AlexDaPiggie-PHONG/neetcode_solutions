import string
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        doodoo = {}
        for c in string.ascii_lowercase:
            doodoo[c] = 0
        for c in s:
            doodoo[c] += 1
        for c in t:
            doodoo[c] -= 1
            if doodoo[c] < 0: 
                return False
        return True
    
s = "xx"
t = "x"
solulu = Solution()
print (solulu.isAnagram(s, t))
