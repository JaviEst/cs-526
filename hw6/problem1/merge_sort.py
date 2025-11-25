def merge_sort(arr: list[int]) -> list[int]:
    a = arr.copy()
    if len(a) <= 1:
        return a

    def _merge(left: list[int], right: list[int]) -> list[int]:
        i = j = 0
        out: list[int] = []
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                out.append(left[i])
                i += 1
            else:
                out.append(right[j])
                j += 1
        out.extend(left[i:])
        out.extend(right[j:])
        return out

    mid = len(a) // 2
    left = merge_sort(a[:mid])
    right = merge_sort(a[mid:])
    return _merge(left, right)