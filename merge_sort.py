def merge_sort(nums: list[int]):
    if len(nums) > 1:
        # get mid point, split into 2 arrays
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]

        merge_sort(left)        # divide the lists
        merge_sort(right)

        # sort left and right into 1 array

        l = 0     # iterators for left and right arrays
        r = 0       # iterator for main array

        while l < len(left) and r < len(right):
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

if __name__ == "__main__":
    nums = [5, 2, 6, 4, 6, 1, 9]
    merge_sort(nums)
    print(nums)
