from collections import defaultdict
class Solution:
    def myfunction(self, s: str, k: int) -> int:
        result = freq = start = 0
        count = defaultdict(str)
        for end in range (len(s)): 
            count[s[end]] = count.get(s[end], 0) + 1
            freq = max(freq, count[s[end]])
                
            while (end - start + 1) - freq > k:
                count[s[start]] -= 1
                start += 1
                freq = max(count.values())

            result = max(result, end - start + 1)
        return result 
    
    def comparefunction(self, s: str, k: int) -> int:
        res = 0
        charSet = set(s)

        for c in charSet:
            count = l = 0
            for r in range(len(s)):
                if s[r] == c:
                    count += 1

                while (r - l + 1) - count > k:
                    if s[l] == c:
                        count -= 1
                    l += 1

                res = max(res, r - l + 1)
        return res
    
alex = Solution()

s = "XYYX" #4
k = 2
s = "ABAB" #1
k = 0
s="AAABABB" #5
k = 1


#Tools
from time import perf_counter
import argparse
import os
alex = Solution()
os.system('cls')

#Show progress bar
def progress (prog, total):
    percent = 100 * (prog / total) 
    bar = '█' * int(percent) + '-' * int(100 - percent)
    print (f"\r|{bar}| {percent:.2f}%", end = "\r")

#Modes to choose from 
def parse():
    mode = argparse.ArgumentParser()
    command = mode.add_mutually_exclusive_group()
    command.add_argument("--t", action = "store_true")
    command.add_argument("--a", action = "store_true")
    return mode.parse_args()

#Compare time performance
me = neetcode = iter = 0
minTime, maxTime = 1000, 0

args = parse()
show_time = args.t
show_all= args.a

trials = 20

for _ in range (trials):
    iter += 1
    start = perf_counter()
    for _ in range (int(1e4)):
        alex.myfunction(s, k)

    time1 = perf_counter() - start
    minTime = min(minTime, time1)
    maxTime = max(maxTime, time1)

    start = perf_counter()
    for _ in range (int(1e4)):
        alex.comparefunction(s, k)
    time2 = perf_counter() - start

    if show_time or show_all:
        print (f"\nTEST: time1 = {time1 * 1000: .6f} ms")
        print (f"TEST: time2 = {time2 * 1000: .6f} ms\n")

    if time2 < time1: neetcode += 1
    else: me += 1

    if not show_time:
        progress(iter, trials)

print()
print('\n                                DONE TESTING!!!')
print ('------------------------------------------------------------------------------------------')
if me > neetcode: print ("REPORT: My performance is better")
else: print ("neetcode is better")
print (f"REPORT: DONE TESTING HIHI!!!")
print (f"REPORT: My performance over 200 time is: {me / trials * 100}%")
print (f"REPORT: Min time is {minTime* 1000: .3f} ms and max time is {maxTime* 1000: .3f} ms")
print ('------------------------------------------------------------------------------------------')