class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if not s1 or len(s1) > len(s2):
            return False
        
        window = {chr(i + ord('a')) : 0 for i in range (26)}
        target = window.copy()
        for i in range (len(s1)):
            target[s1[i]] += 1
            window[s2[i]] += 1
        matches = 26
        for i in range (26):
            char = chr(i + ord('a'))
            if target[char] != window[char]:
                matches -= 1
        if matches == 26:
            return True
        
        start = 0 
        start_char = s2[0]
        if window[start_char] == target[start_char]:
            matches -= 1
        window[start_char] -= 1
        if window[start_char] == target[start_char]:
            matches += 1
        
        start = 1
        for end in range (len(s1), len(s2)):
            end_char = s2[end]
            if window[end_char] == target[end_char]:
                matches -= 1
            window[end_char] += 1
            if window[end_char] == target[end_char]:
                matches += 1
            
            if matches == 26: 
                return True
        
            start_char = s2[start]
            if window[start_char] == target[start_char]:
                matches -= 1
            window[start_char] -= 1
            if window[start_char] == target[start_char]:
                matches += 1
            start += 1
        return False
        
# s1="abc"
# s2="cccccbabbbaaaa"
# s1="ab"
# s2="eidboaaoo"
s1="a"
s2="ab"
phongteo = Solution()
print (phongteo.checkInclusion(s1, s2))