import time
import sys
import ctypes
class PyObject(ctypes.Structure):
    _fields_ = [("refcnt", ctypes.c_long)]
def nthFib(n):
    cache = {}
    def recurse(num):
        if num in cache:
            return cache[num]
        if num == 0 or num == 1:
            return 1
        result = recurse(num - 1) + recurse(num - 2)
        cache[num] = result
        return result

    return recurse(n)

def nthFibRecursive(n):
    if n <= 1:
        return 1
    return nthFibRecursive(n-1) + nthFibRecursive(n-2)

def main():
    start = time.perf_counter()
    term_number = int(sys.argv[1])
    fibonacci_answer, cache_id = nthFib(term_number)
    end = time.perf_counter()
    print(fibonacci_answer)
    print(start - end)
    print(cache_id)
    print(PyObject.from_address(cache_id).refcnt)

main()
