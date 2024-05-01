# defines the shell sort 3 function that uses the gap sequence 2^p*3^q largest number less than n... 1

def shell_sort3(nums: list[int]):
    # find and precompute the gap sequence for given n
    n = len(nums)
    sequence = [1]
    q = 1
    next_double = 0
    while (sequence[-1] <= n):
        while (sequence[next_double]*2 < 3**q):
            sequence.append(sequence[next_double]*2)
            next_double += 1
            if (sequence[-1] > n):
                break
        if (sequence[-1] > n):
            break
        sequence.append(3**q)
        q += 1
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