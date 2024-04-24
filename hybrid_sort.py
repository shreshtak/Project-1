import merge_sort, insertion_sort

def hybrid_sort(nums, h):
    # if nums length > H:
    #   merge sort on nums
    # else:
    #   insertion sort on nums

    if len(nums) > h:
        # merge sort

        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]

        hybrid_sort(left, h)        # divide the lists
        hybrid_sort(right, h)

        # merge
        l = 0     # iterators for left and right arrays
        r = 0     # iterator for main array

        while l < len(left) and r < len(right):     # len of left and right must be at least 1
            if left[l] < right[r]:
                nums[l + r] = left[l]
                l += 1
            else:
                nums[l + r] = right[r]
                r += 1

        # add the extra values to the array
        while l < len(left):
            nums[l + r] = left[l]
            l += 1
        
        while r < len(right):
            nums[l + r] = right[r]
            r += 1
    
    else:
        # insertion sort

        if len(nums) <= 1 :
            return
        
        for i in range(1, len(nums)):
            j = i-1
            while j >= 0:
                if (nums[j] > nums[j+1]) :
                    temp = nums[j+1]
                    nums[j+1] = nums[j]
                    nums[j] = temp
                j -= 1
    
    return


def hybrid_sort1(nums: list[int]):
    # H = n^0.2

    h = len(nums)**0.2
    hybrid_sort(nums, h)

def hybrid_sort2(nums):

    h = len(nums)**0.4
    hybrid_sort(nums, h)

def hybrid_sort3(nums):

    h = len(nums)**0.6
    hybrid_sort(nums, h)
        
    
if __name__ == '__main__' :
    nums = [5, 2, 6, 4, 6, 1, 9]
    hybrid_sort1(nums)
    print(nums)
    hybrid_sort2(nums)
    print(nums)
    hybrid_sort3(nums)
    print(nums)