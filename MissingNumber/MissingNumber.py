class Solution1:
	def missingNumber(self, numbers):
		n = len(numbers) + 1
		sum = n * (n + 1) / 2
		number_sum = sum(numbers)
		result = sum - number_sum
		return result

class Solution2:
	def missingNumber(self, numbers):
		n = len(numbers) + 1
		numbers_xor=0
		for i in numbers:
			numbers_xor ^= i
		total_xor = 0
		for j in range(len(numbers) + 1):
			total_xor ^= j
		return number_xor ^ total_xor
