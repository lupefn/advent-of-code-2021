with open("day3data.txt") as file:
	lines = file.read().split("\n")

def part1(nums):
	bitCount = len(nums[0])
	totalNum = len(nums)
	onesCount = [0] * bitCount
	for num in nums:
		for i in range(0,bitCount):
			if num[i] == "1":
				onesCount[i] += 1
	common = ["0" if ((totalNum - x) > x) else "1" for x in onesCount]
	least = ["0" if x == "1" else "1" for x in common]
	gamma = "".join(common)
	epsilon = "".join(least)
	return int(gamma,2) * int(epsilon,2)

def part2(nums):
	bitCount = len(nums[0])
	mostCommon = [0] * bitCount
	if len(nums) != 1:
		for b in range(bitCount):
			currOnesTally = 0
			numsToDelete = []
			for n in range(len(nums)):
				if nums[n][b] == "1":
					currOnesTally += 1
			if currOnesTally > (len(nums) - currOnesTally):
				mostCommon[b] = "1"
			else:
				mostCommon[b] = "0"
			for o in range(len(nums)):
				if nums[o][b] != mostCommon[b]:
					numsToDelete.append(o)
			for x in range(len(numsToDelete)):
				print('index to remove', x)
				print('length of nums', len(nums))
				nums.pop(numsToDelete[x])
	return nums


if __name__ == "__main__":
	print(part1(lines)) # returns 852500
	print(part2(lines)) 