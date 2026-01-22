class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        alphabet = {}
        start = 0
        size = len(s)
        result = 0

        for end in range (size):
            window = end - start + 1
            alphabet[s[end]] = alphabet.get(s[end], 0) + 1
            while window - max(alphabet.values()) > k:
                start += 1
                if start > end or start >= size: 
                    break 
                alphabet[s[start - 1]] -= 1
                window -= 1

            result = max(window, result)
        return result
    
phongteo = Solution()
input_string = "ABAA"
k=0
print(phongteo.characterReplacement(input_string, k)) 