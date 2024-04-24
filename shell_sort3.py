import math
def shell_sort3(nums: list[int]):
   
    nums_len = len(nums) 

    gaps = [1]
    p = 0
    found = False
    while not found:
        q = 0
        while q <= p:
            g1 = (2**p) * (3**q)
            g2 = (2**q) * (3**p)
            if g1 > 1 and g1 < nums_len:
                if g1 not in gaps: 
                    gaps.append(g1) 
            if g2 > 1 and g2 < nums_len:
                if g2 not in gaps: 
                    gaps.append(g2)  
            if g1 >= nums_len or g2 >= nums_len:
                found = True    # done w loops
            q += 1
        p += 1
    gaps.sort()
    gaps.reverse()  # descending order
    
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
    # shell_sort3(nums)
    # print(nums)
    pass