class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or t == "" or len(s) < len(t): 
            return ""
        
        window, target = {}, {}
        for c in t:
            target[c] = target.get(c, 0) + 1
            window[c] = 0

        have, need = 0, len(target)
        result, result_length = [-1,-1], len(s) + 1
        start = 0

        for end in range (len(s)):
            c = s[end]
            if c in target: 
                window[c] += 1
                if window[c] == target[c]:
                    have += 1
            while have == need:
                c_start = s[start]
                length = end - start + 1
                if length < result_length: 
                    result_length = length 
                    result = [start, end]

                if c_start in target:
                    window[c_start] -= 1
                    if window[c_start] < target[c_start]:
                        have -= 1
                start += 1
        start, end = result
        return s[start : end + 1]
            
            
phongteo = Solution()
s="ADOBECODEBANC"
t="ABC"
print (phongteo.minWindow(s,t))