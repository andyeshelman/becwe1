from random import randint

def quicksort(arr, key=None):
    if key is None:
        _quicksort(arr, 0, len(arr) - 1)
    else:
        _keysort(arr, 0, len(arr) - 1, key)

def _quicksort(arr, lo, hi):
    if hi <= lo:
        return
    pivot = arr[randint(lo,hi)]
    i = lo
    j = hi
    while True:
        while arr[i] < pivot:
            i+= 1
        while arr[j] > pivot:
            j -= 1
        if j <= i:
            break
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1
    _quicksort(arr, lo, i - 1)
    _quicksort(arr, j + 1, hi)

def _keysort(arr, lo, hi, key):
    if hi <= lo:
        return
    pivot = key(arr[randint(lo,hi)])
    i = lo
    j = hi
    while True:
        while key(arr[i]) < pivot:
            i+= 1
        while key(arr[j]) > pivot:
            j -= 1
        if j <= i:
            break
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1
    _keysort(arr, lo, i - 1, key)
    _keysort(arr, j + 1, hi, key)

if __name__ == "__main__":
    tests = []
    for _ in range(100):
        data = [randint(1,99) for _ in range(100)]
        pysort = sorted(data)
        quicksort(data)
        tests.append(data == pysort)
    print(all(tests))