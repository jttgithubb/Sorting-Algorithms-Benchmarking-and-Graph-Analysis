# defines the shell sort 2 function that uses the gap sequence 2**k + 1 starting at k=logn...1
import math

def shell_sort2(nums: list[int]):
    # store the initial size of nums and starting gap value
    n = len(nums)
    gap = n + 1
    k = int(math.log2(n))
    # while gap is not yet 0
    while gap > 0 and k >= -1:
        for i in range(gap, n):
            temp = nums[i]
            j = i
            # keep sifting i down by gap
            while j >= gap and nums[j - gap] > temp:
                nums[j] = nums[j - gap]
                j -= gap
            nums[j] = temp
        # update gap
        if k > 0:
            gap = 2**k + 1
            k -= 1
        else:
            gap = 1
            k -= 1