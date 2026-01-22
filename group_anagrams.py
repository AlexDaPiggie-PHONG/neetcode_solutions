'''
Docstring for group_anagrams
error
    Before original set {'stop', 'tops', 'hat', 'pots'}
    After original set {'stop', 'tops', 'hat', 'pots'}
    Subset at the end of interation {'cat', 'act'}

'''
import string
def checkAnagram (s, t):
    if len(s) != len(t): 
        return False
    doodoo = {}
    for c in string.ascii_lowercase:
        doodoo[c] = 0
    for c in s: 
        doodoo[c] += 1
    for c in t:
        doodoo[c] -=1
        if doodoo[c] < 0:
            return False
    return True

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        if len(strs) <= 1: return [strs]
        original_lst = strs
        sub_lst = []
        result = []
        while len(original_lst) != 0:
            sub_lst.clear()
            sub_lst.append(original_lst[0])
            for i in range (1, len(original_lst)):        
                if checkAnagram(original_lst[0], original_lst[i]):
                    sub_lst.append(original_lst[i])

            for c in sub_lst:
                original_lst.remove(c)

            result.append(list(sub_lst))
        return result

solulu = Solution()
strs = ["x"]
print (solulu.groupAnagrams(strs))

