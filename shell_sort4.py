# defines the hybrid sort 4 function which uses the sequence 4^(n+1) + 3*2^n + 1 ... 1

def shell_sort4(nums: list[int]):
    n = len(nums)
    k = 0
    sequence = [1]
    while (sequence[-1] <= n):
        next_num = 4**(k+1) + 3 * 2**k + 1
        sequence.append(next_num)
        k += 1
    sequence.pop()
    
    # intialize the state of gap
    gap_idx = len(sequence) - 1
    gap = sequence[gap_idx]
    gap_idx -= 1
    # while gap is not yet 0
    while gap_idx >= -1:
        for i in range(gap, n):
            temp = nums[i]
            j = i
            # keep sifting i down by gap
            while j >= gap and nums[j - gap] > temp:
                nums[j] = nums[j - gap]
                j -= gap
            nums[j] = temp
        # update gap
        gap = sequence[gap_idx]
        gap_idx -= 1