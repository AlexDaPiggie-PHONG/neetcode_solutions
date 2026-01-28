from collections import deque
class Solution:
    def first_function(self, nums: list[int], k: int) -> list[int]:
        if not nums: return []
        if k == 1: return nums
        q = deque()
        result = []
        start = 0
        for idx, char in enumerate(nums):
            while q and char > q[-1]:
                q.pop()
            q.append(char)
            if idx + 1 >= k:
                result.append(q[0])
                if nums[start] == q[0]:
                    q.popleft()
                start += 1
        return result
    
    def second_function(self, nums: list[int], k: int) -> list[int]:
        queue = deque()
        result = []
        # building phase
        for i in range(k):
            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()
            queue.append(i)
        result.append(nums[queue[0]])
        for i in range(k, len(nums)):
            if queue[0] <= i - k:
                queue.popleft()
            while queue and nums[i] > nums[queue[-1]]:
                queue.pop()
            queue.append(i)
            result.append(nums[queue[0]])
        return result

alex = Solution()
nums = [1,2,1,0,4,2,6]
k = 3 #2,2,4,4,6

nums = [1,2,3,2,3,3,6,4,5]
k = 3 #3,3,3,3,6,6,6

nums = [3,2,1,2,2,4,5,6]
k = 3 #3,2,2,4,5,6

nums = [9,8,7,6,11,10,9,8,7]
k = 3 #

#======================= FUNCTIONS END ===================================
                

#Tools
from time import perf_counter
from time import sleep
import argparse
import os
from rich.console import Console

console = Console()

os.system('cls')

#Format color
def print_color (text = "", end = "\n", style = "sea_green2"):
    console.print(f"{text}", end = end, style = style)

#Show progress bar
def progress (prog, total):
    percent = 100 * (prog / total) 
    if total < 500:
        bar = '█' * int(percent // 1.4) + '-' * int((100 - percent) // 1.4)
    else:
        bar = '█' * int(percent // 0.95) + '-' * int((100 - percent) // 0.95)
    print_color (f"\r[bold plum1]│[/bold plum1]{bar}[bold plum1]│[/bold plum1] [bold steel_blue1]{percent:.2f}%[/bold steel_blue1]", end = "\r")

#Modes to choose from 
def parse():
    mode = argparse.ArgumentParser()
    mode.add_argument("--t", action = "store_true", )
    mode.add_argument("--p", action = "store_true")
    mode.add_argument("--num", dest ="num", type = int)
    return mode.parse_args()

#Compare time performance
first = second = iter = 0
minTime1, maxTime1, avg1 = 1e10, 0.0, 0.0
minTime2, maxTime2, avg2 = 1e10, 0.0, 0.0

args = parse()
show_time = args.t
show_progress = args.p

trials = 1000
if args.num:
    trials = int(args.num)
    

for iter in range (1, trials + 1):

    #Estimate each run time
    start = perf_counter()
    for _ in range (1000):
        alex.first_function(nums, k)

    time1 = perf_counter() - start
    minTime1 = min(minTime1, time1)
    maxTime1 = max(maxTime1, time1)
    avg1 += time1 / trials

    start = perf_counter()
    for _ in range (1000):
        alex.second_function(nums, k)
    time2 = perf_counter() - start
    minTime2 = min(minTime2, time2)
    maxTime2 = max(maxTime2, time2)
    avg2 += time2 / trials

    #Update winning score
    if time1 < time2: 
        first += 1
    else: 
        second += 1

    #Display

    if not show_progress:
        print_color (f"\nTEST: time1 = [bold steel_blue1]{time1 * 1000: .6f} ms[/bold steel_blue1]")
        print_color (f"TEST: time2 = [bold steel_blue1]{time2 * 1000: .6f} ms[/bold steel_blue1]")

    if not show_time:
        progress(iter, trials)

#Format output
if not (show_progress or show_time):
    sleep(0.25)
    os.system('cls')

print_color()
print_color(f"\n                                   [bold steel_blue1]DONE TESTING!!![/bold steel_blue1]")
print_color ("                ┌──────────────────────────────────────────────────────────────┐ ")

if first > second:
    print_color ("                │       [bold plum1]REPORT: FIRST function has BETTER performance[bold plum1]          │")
    print_color ("                │                                                              │")
    print_color (f"                │       REPORT: [bold plum1]WINNING RATE[/bold plum1] of [bold plum1]FIRST[/bold plum1] function is: [bold plum1]{first / trials * 100:5.1f}%[/bold plum1]      │")


else: 
    print_color ("                │       [bold underline bold plum1]REPORT: SECOND function has BETTER performance[/bold underline bold plum1]         │")
    print_color ("                │                                                              │")
    print_color (f"                │       REPORT: [bold plum1]WINNING RATE[/bold plum1] of [bold plum1]SECOND[/bold plum1] function is: [bold plum1]{second/ trials* 100:5.1f}%[/bold plum1]     │")

print_color ("                │                                                              │")
print_color (f"                │       REPORT: RUN TIME OF FIRST FUNCTION:                    │\r")                  
print_color (f"\r                │       ┌───────────────────────┐                              │\n"
       f"                │       │ min     = [bold steel_blue1]{minTime1* 1000: 8.3f} ms[/bold steel_blue1] │                              │\n"
       f"                │       │ max     = [bold steel_blue1]{maxTime1* 1000: 8.3f} ms[/bold steel_blue1] │                              │\n"
       f"                │       │ average = [bold steel_blue1]{avg1 * 1000: 8.3f} ms[/bold steel_blue1] │                              │\n"
       f"                │       └───────────────────────┘                              │\r")

print_color (f"\r                │       REPORT: RUN TIME OF SECOND FUNCTION:                   │\r")
print_color (f"\r                │       ┌───────────────────────┐                              │\n"
       f"                │       │ min     = [bold steel_blue1]{minTime2* 1000: 8.3f} ms[/bold steel_blue1] │                              │\n"
       f"                │       │ max     = [bold steel_blue1]{maxTime2* 1000: 8.3f} ms[/bold steel_blue1] │                              │\n"
       f"                │       │ average = [bold steel_blue1]{avg2 * 1000: 8.3f} ms[/bold steel_blue1] │                              │\n"
       f"                │       └───────────────────────┘                              │")
print_color (f"                └──────────────────────────────────────────────────────────────┘")
