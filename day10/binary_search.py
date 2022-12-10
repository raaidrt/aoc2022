def binsearch(f, lo, hi):
    if f(lo): return lo
    elif not f(hi): return None
    while hi - lo > 1:
        mid = (hi + lo) // 2
        if f(mid):
            hi = mid
        else:
            lo = mid
    return hi
