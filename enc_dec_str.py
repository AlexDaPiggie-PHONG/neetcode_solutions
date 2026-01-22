'''
Docstring for enc_dec_str
["", ""]
hello, world

5#hello5#world

0#0#
0123
len 
Search for the first 
'''
class Solution:
    def encode(self, strs: list[str]) -> str:
        if not strs:
            return ""
        result = ""
        for sub_str in strs:
            length = len(sub_str)
            result += str(length) + '#' + sub_str
        return result

    def decode(self, s: str) -> list[str]:
        if s == "":
            return []
        result = []
        i = s.find('#')
        # print ("DEBUG: # position before iteration", i)
        length = int(s[:i])
        word = s[i + 1:i+1+length]
        result.append(word)
        # print ("DEBUG: RESULT before interation is", result)
        # print ("DEBUG: length of string is:", len(s))
        # print ("DEBUG: encoded string:", s)
        while i < len(s):
            # print ("DEBUG: START ITERATION ==========================================")
            start = i + length + 1
            # print ("DEBUG: start position is:", start)
            # print ("DEBUG: substring from start onward is:", s[start:])
            i = start + s[start:].find('#')
            if start >= len(s) - 1:
                return result
            # print ("DEBUG: position of # is: ", i)
            if i >= len(s): 
                return result
            length = int(s[start: i])
            # print ("DEBUG: length is:", length)
            word = s[i + 1 : i + 1 + length]
            
            result.append(word)
            # print ("DEBUG: Result of this interation is:", result)z
            # print ("DEBUG: END ITERATION ==================================")

        return result
    
solulu = Solution()
dummy_input = ["\""]
print (solulu.encode(dummy_input))
print (solulu.decode(solulu.encode(dummy_input)))