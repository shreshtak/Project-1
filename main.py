from insertion_sort import insertion_sort
from merge_sort import merge_sort
from shell_sort1 import shell_sort1
from shell_sort2 import shell_sort2
from shell_sort3 import shell_sort3
from shell_sort4 import shell_sort4
from hybrid_sort import hybrid_sort1, hybrid_sort2, hybrid_sort3
import math, random, time


# TO-DOS:
# - Create the following arrays to test input:
#   1. Uniformly distributed permutations (sizes: 100, 500, 1000, 2500, 5000)
#   2. Almost-sorted permutations (sizes: 100, 500, 1000, 2500, 5000)
#   3. Reverse sorted permutation (sizes: 100, 500, 1000, 2500, 5000)
# - Run each input with each sorting algorithm 10 times
# - Get the average runtime of the 10 runs
# - plot for each input size on a log log plot for each algorithm 
#    1. Insertion-sort and merge-sort for each permutation (3 plots)
#    2. Shell sort versions together, for each permutation (3 plots)
#    3. Hybrid sort versions together, for each permutation (3 plots)
#    4. Plotting different Shell sort algorithms and different Hybrid-sort algorithms for each permutation
#    5. For each algorithm, plotting all versions, on all permutations in a single plot (1 plot for each algorithm)


def get_avg_runtime(arr, algorithm):
    # run algorithm with given array 10 times
    # return: average runtime 

    runtimes = []

    for _ in range(10):
        start = time.time()
        algorithm(arr)
        end = time.time()
        runtimes.append(end-start)
    
    return (sum(runtimes) / len(runtimes))


def get_inputs():

    # create the input arrays, sizes: 100, 500, 1000, 2500, 5000
    sizes = [100, 500, 1000, 2500, 5000]    

    uniform_input = []  # array of uniformly distributed permutations
    almost_sorted_input = []  # array of almost sorted permutations
    reverse_sorted_input = []  # array of reverse sorted permutations
    for s in sizes:
        sub_arr = [i for i in range(s)]
        uniform_input.append(sub_arr)
    
    # almost sorted
    for i, arr in enumerate(uniform_input):
        temp_arr = arr
        num_swaps = math.floor(2 * math.log(sizes[i]))
        for j in range(num_swaps):
            x = random.randint(0, sizes[i]-1)   # get 2 random indices in the range of the array
            y = random.randint(0, sizes[i]-1)
            temp_arr[x], temp_arr[y] = temp_arr[y], temp_arr[x]     # swap the values at indices x and y
        
        almost_sorted_input.append(temp_arr)    # add almost sorted array to input arr

    for arr in uniform_input:
        reverse_sorted_input.append(list(reversed(arr)))

    return uniform_input, almost_sorted_input, reverse_sorted_input


def main():

    # get the input arrays
    uniform_input, almost_sorted_input, reverse_sorted_input = get_inputs()
    # store runtime data for each sorting algorithm in dictionary
    runtime_results = {}   
    # format: 
    # {
    # "insertion": {
    #   "uniform":[avg runtimes for 100, 500, 1000, 2500, 5000], 
    #   "almost_sorted": [avg runtimes for 100, 500, 1000, 2500, 5000],
    #   "reversed": [avg runtimes for 100, 500, 1000, 2500, 5000]
    #  },
    #  "merge_sort": {
    #    "uniform":[avg runtimes for 100, 500, 1000, 2500, 5000], 
    #    "almost_sorted": [avg runtimes for 100, 500, 1000, 2500, 5000],
    #    "reversed": [avg runtimes for 100, 500, 1000, 2500, 5000]
    #   },
    #   ...
    # }   

    # run the algorithms with all input combinations, get all runtime data

    # pseudocode:
    # for algo in  algorithm:
    #   for each input in inputs:
    #       for arr in input:
    #           call algo 10 times with arr, time and get average of 10 runs

    inputs = [uniform_input, almost_sorted_input, reverse_sorted_input]
    algorithms = [insertion_sort, merge_sort, shell_sort1, shell_sort2, shell_sort3, shell_sort4, hybrid_sort1, hybrid_sort2, hybrid_sort3]

    algo_keys = ["insertion_sort", "merge_sort", "shell_sort1", "shell_sort2", "shell_sort3", "shell_sort4", "hybrid_sort1", \
                 "hybrid_sort2", "hybrid_sort3"]
    input_keys = ["uniform", "almost_sorted", "reversed"]

    print("Runtime results for algorithms:")
    for i, algo in enumerate(algorithms):
        runtime_results[algo_keys[i]] = {}
        print(algo_keys[i])
        for j, input in enumerate(inputs):
            input_runtimes = []     # avg runtimes for arr sizes 100...5000 for input permutation j
            for arr in input:
                input_runtimes.append(get_avg_runtime(arr, algo))  
            runtime_results[algo_keys[i]][input_keys[j]] = input_runtimes   # ex: {"insertion": { "uniform": [avg runtimes for 100, 500, 1000, 2500, 5000]}}
            print(f"\t{input_keys[j]}: {str(input_runtimes)}")
            

    return runtime_results

if __name__ == "__main__":
   main()

    # print(str(runtime_results))


    

    
