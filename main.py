from insertion_sort import insertion_sort
from merge_sort import merge_sort
from shell_sort1 import shell_sort1
from shell_sort2 import shell_sort2
from shell_sort3 import shell_sort3
from shell_sort4 import shell_sort4
from hybrid_sort import hybrid_sort1, hybrid_sort2, hybrid_sort3
import math, random, time
import numpy as np
from matplotlib import pyplot as plt


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

def plot_data(axis, x_axis, runtime_results, title, algorithms, inputs, labels):

    colors = ['blue', 'red', 'green', 'yellow', 'purple', 'orange', 'brown', 'cyan', 'pink']
    linestyles = ['solid', 'dashed', 'dotted']

    axis.set_title(title, fontsize='8')
    axis.set_xlabel('Input Size (# of elements)', fontsize='8')
    axis.set_ylabel('Runtime (ms)', fontsize='8')

    axis.set_xscale('log', base=2)  # Set x-axis scale to logarithmic with base 2
    axis.set_yscale('log', base=2)  # Set y-axis scale to logarithmic

    for i, alg in enumerate(algorithms):
        for j, p in enumerate(inputs):
            axis.plot(x_axis, runtime_results[alg][p], linestyle=linestyles[j], color=colors[i], marker='.')

    axis.legend(labels=labels, loc='best', facecolor='white', edgecolor='black', fontsize='6', labelcolor='black')

def get_avg_runtime(arr, algorithm):
    # run algorithm with given array 10 times
    # return: average runtime 

    runtimes = []

    for _ in range(10):
        start = time.time()
        algorithm(arr)
        end = time.time()
        runtimes.append((end-start)*1000)
    
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

    f = open('results.txt', 'w')
    # get the input arrays
    uniform_input, almost_sorted_input, reverse_sorted_input = get_inputs()
    print("Created input data...")
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

    inputs = [uniform_input, almost_sorted_input, reverse_sorted_input]
    algorithms = [insertion_sort, merge_sort, shell_sort1, shell_sort2, shell_sort3, shell_sort4, hybrid_sort1, hybrid_sort2, hybrid_sort3]
    input_keys = ["uniform", "almost_sorted", "reversed"]

    algo_keys = ["insertion_sort", "merge_sort", "shell_sort1", "shell_sort2", "shell_sort3", "shell_sort4", "hybrid_sort1", \
                 "hybrid_sort2", "hybrid_sort3"]

    print("Calculating runtimes.....")
    f.write("Runtime results for algorithms (in ms):\n")
    for i, algo in enumerate(algorithms):
        runtime_results[algo_keys[i]] = {}
        f.write(algo_keys[i] + "\n")
        for j, input in enumerate(inputs):
            input_runtimes = []     # avg runtimes for arr sizes 100...5000 for input permutation j
            for arr in input:
                input_runtimes.append(get_avg_runtime(arr, algo))  
            runtime_results[algo_keys[i]][input_keys[j]] = input_runtimes   # ex: {"insertion": { "uniform": [avg runtimes for 100, 500, 1000, 2500, 5000]}}
            f.write(f"\t{input_keys[j]}: {str(input_runtimes)}\n")
    
    f.write("\n\n")

    # plot the data on log log plots
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3)
    input_keys = ["uniform", "almost_sorted", "reversed"]
    x_axis = [100, 500, 1000, 2500, 5000]

    # **** COMMENT OUT ONE SECTION AT A TIME ***

    # For the sorting algorithms
    # plot_data(ax1, x_axis, runtime_results, "Runtimes for Insertion_sort and Merge sort", ['insertion_sort', 'merge_sort'], input_keys, input_keys)
    # plot_data(ax2, x_axis, runtime_results, "Runtimes for 4 Shell sort algorithms", ["shell_sort1", "shell_sort2", "shell_sort3", "shell_sort4"], input_keys, input_keys)
    # plot_data(ax3, x_axis, runtime_results, "Runtimes for Hybrid sort algorithms", ["hybrid_sort1", "hybrid_sort2", "hybrid_sort3"], input_keys, input_keys)

    # comparing permutations between each sorting algorithm
    # plot_data(ax1, x_axis, runtime_results, "Runtime of Uniform Permutations", algo_keys, ['uniform'], algo_keys)
    # plot_data(ax2, x_axis, runtime_results, "Runtime of Almost-Sorted Permutations", algo_keys, ['almost_sorted'], algo_keys)
    # plot_data(ax3, x_axis, runtime_results, "Runtime of Reversed Permutations", algo_keys, ['reversed'], algo_keys)

    # plot_data(ax1, x_axis, runtime_results, "Runtime of Uniform Permutations", algo_keys, ['uniform'], algo_keys)
    # plot_data(ax2, x_axis, runtime_results, "Runtime of Almost-Sorted Permutations", algo_keys, ['almost_sorted'], algo_keys)
    # plot_data(ax3, x_axis, runtime_results, "Runtime of Reversed Permutations", algo_keys, ['reversed'], algo_keys)

    plt.show()

    # get slopes of 

    f.close()
    return runtime_results

if __name__ == "__main__":
   main()

    # print(str(runtime_results))


    

    
