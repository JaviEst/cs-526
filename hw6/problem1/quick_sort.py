def quick_sort(arr: list[int]) -> list[int]:
    a = arr.copy()

    def _quicksort(lo: int, hi: int) -> None:
        if lo >= hi:
            return
        pivot = a[(lo + hi) // 2]
        i, j = lo, hi
        while i <= j:
            while a[i] < pivot:
                i += 1
            while a[j] > pivot:
                j -= 1
            if i <= j:
                a[i], a[j] = a[j], a[i]
                i += 1
                j -= 1
        if lo < j:
            _quicksort(lo, j)
        if i < hi:
            _quicksort(i, hi)

    _quicksort(0, len(a) - 1)
    return a