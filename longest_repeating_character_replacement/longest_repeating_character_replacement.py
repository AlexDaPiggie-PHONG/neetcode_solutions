class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) <= 1: return s
        result = start = maxCount = 0
        count = [0] * 26
        for end in range (len(s)):
            #replace = length - max count
            char = ord(s[end]) - 65
            count[char] += 1
            maxCount = max(count[char], maxCount)
            
            while (end - start + 1) - maxCount > k: 
                count[ord(s[start]) - 65] -= 1
                start += 1
                maxCount = max(count)
                
            result = max(end - start + 1, result)
        return result 
    
alex = Solution()

s = "XYYX" #4
k = 2
s="AAABABB" #5
k = 1
s = "ABAB" #1
k = 0
print (alex.characterReplacement(s, k))