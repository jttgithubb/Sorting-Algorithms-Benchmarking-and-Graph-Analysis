# defines the shell sort 1 function that uses the original gap sequence

def shell_sort1(nums: list[int]):
    # store the initial size of nums and starting gap value
    n = len(nums)
    gap = n // 2
    # while gap is not yet 0
    while gap > 0:
        for i in range(gap, n):
            temp = nums[i]
            j = i
            # keep sifting i down by gap
            while j >= gap and nums[j - gap] > temp:
                nums[j] = nums[j - gap]
                j -= gap
            nums[j] = temp
        # update gap
        gap //= 2