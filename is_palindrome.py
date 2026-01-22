class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s or len(s) == 1: return True
        result = ""
        for c in s:
            if (c >= 'a' and c <= 'z') or (c >= 'A' and c <= 'Z') or c.isnumeric():
                result += c
        result = result.lower()
        size = len(result)
        for i in range (size):
            if result[i] != result[size - 1 - i]:
                return False
        return True

metumap = Solution()
input = input()
print (metumap.isPalindrome(input))

