class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        size = len(s)
        if size <= 1: return size
        substr = set()
        maxLength = 0
        for i in range (size):
            if s[i] not in substr:
                substr.add(s[i])
                for j in range (i + 1, size):
                    if s[j] not in substr:
                        substr.add(s[j])
                    else:
                        length = len(substr)
                        if length > maxLength: maxLength = length
                        substr.clear()
                        break

            else:
                substr.add(s[i])
                length = len(substr)
                if length > maxLength: maxLength = length
                substr.clear()

        return maxLength
        

s = "aabcds"
solulu = Solution()
print (solulu.lengthOfLongestSubstring(s))