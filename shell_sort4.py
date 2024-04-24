import math
def shell_sort4(nums: list[int]):
    # 4^(n+1) + 3*2^n + 1
   
    nums_len = len(nums) 

    gaps = [1]
    
    i = 0
    while True:
        g = 4**(i+1) + (3 * (2**i)) + 1
        if g > 1 and g < nums_len:
            gaps.append(g)
        elif g >= nums_len:
            break

        i += 1
    
    for gap in gaps:    
        for i in range(gap, nums_len):
            temp = nums[i]
            j = i
            while (j >= gap and temp < nums[j-gap]):
                nums[j] = nums[j-gap]
                j -= gap
            nums[j] = temp


if __name__ == "__main__":
    # nums = [6, 1, 2, 19, 31, 54, 45, 47, 76]
    # shell_sort4(nums)
    # print(nums)
    pass