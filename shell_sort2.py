import math
def shell_sort2(nums: list[int]):
   
    nums_len = len(nums) 
    k = math.ceil(math.log2(nums_len))

    gaps = []
    while k > 0:
        gaps.append(2**k + 1)
        k -= 1
    
    gaps.append(1) # add 1

    for gap in gaps:    
        for i in range(gap, nums_len):
            temp = nums[i]
            j = i
            while (j >= gap and temp < nums[j-gap]):
                nums[j] = nums[j-gap]
                j -= gap
            nums[j] = temp


if __name__ == "__main__":
    # nums = [6, 1, 2, 19, 31, 54, 45, 47]
    # shell_sort2(nums)
    # print(nums)
    pass