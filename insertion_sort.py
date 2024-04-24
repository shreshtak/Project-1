# Example file: insertion_sort.py

# Each sorting function should accept a list of integers as the single required
# parameter, as shown below. The input list should be sorted upon completion.
def insertion_sort(nums: list[int]):

	# if nums is length 0 or 1, return
	
	# for each element in nums[1:]
		# get the current element
		# for each sorted element in nums[:i]
			# if current > sorted element, swap the elements 
		# insert current in nums 
	
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
		