# Benchmark the performance of specfic sorting algorithms on specific permutations of data
from insertion_sort import insertion_sort
from merge_sort import merge_sort
from hybrid_sort1 import hybrid_sort1
from hybrid_sort2 import hybrid_sort2
from hybrid_sort3 import hybrid_sort3
from shell_sort1 import shell_sort1
from shell_sort2 import shell_sort2
from shell_sort3 import shell_sort3
from shell_sort4 import shell_sort4
import argparse
import random
import math
import time
from enum import Enum
from pathlib import Path


DATA_DIRECTORY = Path('data')

class PermutationType(Enum):
    UNIFORMLY_DISTRIBUTED = 'uniform'
    REVERSE_SORTED = 'reverse'
    ALMOST_SORTED = 'almost'

SORTING_ALGORITHMS = {
    'insertion_sort': insertion_sort,
    'merge_sort': merge_sort,
    'shell_sort1': shell_sort1,
    'shell_sort2': shell_sort2,
    'shell_sort3': shell_sort3,
    'shell_sort4': shell_sort4,
    'hybrid_sort1': hybrid_sort1,
    'hybrid_sort2': hybrid_sort2,
    'hybrid_sort3': hybrid_sort3
}

parser = argparse.ArgumentParser(
    prog= 'Benchmark', 
    description= 'Benchmark the performance of sorting algorithms on specific permutations of data.', 
    epilog= 'Happy benchmarking! :)')

parser.add_argument('size', type=int, help='Size of the input list')
parser.add_argument('permutation', type=PermutationType, help='Permutation of the input list')
parser.add_argument('algorithm_name', choices=SORTING_ALGORITHMS.keys(), help='Name of the sorting algorithm')

def fy_shuffle(input_list):
    for i in range(len(input_list) - 1, 0, -1):
        j = random.randint(0, i)
        input_list[i], input_list[j] = input_list[j], input_list[i]

def almost_shuffle(input_list):
    n = len(input_list)
    num_pairs = int(2 * math.log2(n))
    for p in range(num_pairs):
        i, j = random.randint(0, n - 1), random.randint(0, n - 1)
        input_list[i], input_list[j] = input_list[j], input_list[i]
    
def generate_random_list(size: int, permutation: PermutationType):
    nums = [i for i in range(size)]
    if permutation == PermutationType.UNIFORMLY_DISTRIBUTED: 
        fy_shuffle(nums)
    if permutation == PermutationType.REVERSE_SORTED:
        nums.reverse()
    if permutation == PermutationType.ALMOST_SORTED:
        almost_shuffle(nums)
    return nums

def get_data_path(permutation: PermutationType, algorithm_name: str):
    directory = DATA_DIRECTORY / algorithm_name
    directory.mkdir(parents=True, exist_ok=True)
    return (directory / permutation.value).with_suffix('.csv')

def run_benchmark(size: int, permutation: PermutationType, algorithm_name: str, algorithm):
    nums = generate_random_list(size, permutation)
    start_time = time.process_time_ns()
    algorithm(nums)
    end_time = time.process_time_ns()
    elapsed_time = end_time - start_time
    return elapsed_time

if __name__ == "__main__":
    args = parser.parse_args()
    data_path = get_data_path(args.permutation, args.algorithm_name)
    with open(data_path, 'a') as f:
        for i in range(10):
            nums = generate_random_list(args.size, args.permutation)
            t = run_benchmark(args.size, args.permutation, args.algorithm_name, SORTING_ALGORITHMS[args.algorithm_name])
            f.write(f'{args.size} {t}\n')
    