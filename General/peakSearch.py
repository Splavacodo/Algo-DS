def peakSearch(nums: list[int], i: int, j: int) -> int: 
    """
    Suppose that you are given an array A[1 · · · n] of n entries, with each entry having
    a distinct number (that is, no two numbers of A are equal). You are told that the sequence
    of values A[1], A[2], . . . , A[n] is unimodal: For some index p between 1 and n, the values in the
    array entries increase up to position p in A and then decrease the rest of the way until position
    n. (So if you were to draw a plot with the array index i on the x-axis and the value of the entry
    A[i] on the y-axis, the plotted points would rise until x-value p, where they would achieve their
    maximum, and then fall from there on.)

    You would like to find the “peak entry” p without having to read the entire array – in fact, by
    reading as few entries of A as possible. Show how to find the entry p by reading at most O(log n)
    entries of A. In other words, design an O(log n) time algorithm to find the peak entry p.
    """
    if (j - i) <= 1: 
        return max(nums[i], nums[j])
    
    mid = (j + i)//2

    if nums[mid] > nums[mid + 1]: 
        return peakSearch(nums, i, mid)
    else: 
        return peakSearch(nums, mid + 1, j)

nums = [1, 5, 3]
print("Peak:", peakSearch(nums, 0, len(nums) - 1))