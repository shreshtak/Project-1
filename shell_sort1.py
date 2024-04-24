import math
def shell_sort1(nums: list[int]):
    # sequence: [n/2^k], ..., 1, for k=1,2,...,log n
    # gap:  n/2^k

    # python pseudocode:
    # calculate gap using formula
    # while gap > 0:
    #    for i in range(gap, a.length):
    #        temp = a[i]
    #        j = i
    #        while (j >= gap and temp < a[j-gap]):
    #            a[j] = a[j-gap]
    #            j -= gap
    #        a[j] = temp
   
    nums_len = len(nums) 
    k = 1    # k = 1, 2, ... , log(n)
    while ((math.floor(nums_len // math.pow(2,k))) > 0):    # when k = log(n), gap = 0
        gap = math.floor(nums_len // math.pow(2,k))
        for i in range(gap, nums_len):
            temp = nums[i]
            j = i
            while (j >= gap and temp < nums[j-gap]):
                nums[j] = nums[j-gap]
                j -= gap
            nums[j] = temp

        k += 1


if __name__ == "__main__":
    # nums = [6, 1, 2, 19, 31, 54, 45, 47]
    # shell_sort1(nums)
    # print(nums)
    pass