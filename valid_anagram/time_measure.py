from time import perf_counter
import valid_anagram


def time_measure(function, *args, trials: int = 5):
    total = 0.0
    for _ in range(trials):
        start = perf_counter()
        function(*args)
        total += perf_counter() - start
    return total / trials


program = valid_anagram.Solution()
s = "jar"
t = "jam"
print(f"{time_measure(program.isAnagram, s, t, trials=10) * 1000:.10f} ms")
from time import perf_counter
import valid_anagram

def time_measure (function, trials: int = 5):
    total = 0.0
    for _ in range(trials):
        start = perf_counter()
        function
        total += perf_counter() - start
    return total / trials

alex = valid_anagram.main()
print (f"{time_measure(alex, trials = 10) * 1000: .10f}")