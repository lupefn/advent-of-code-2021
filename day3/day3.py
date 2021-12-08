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
	oxygenCopy = nums.copy()
	co2Copy = nums.copy()
	mostCommon = [0] * bitCount
	for b in range(bitCount):
		currOnesTally = 0
		numsToDelete = []
		for n in range(len(oxygenCopy)):
			if oxygenCopy[n][b] == "1":
				currOnesTally += 1
		if currOnesTally >= (len(oxygenCopy) - currOnesTally):
			mostCommon[b] = "1"
		else:
			mostCommon[b] = "0"
		for o in range(len(oxygenCopy)):
			if oxygenCopy[o][b] != mostCommon[b]:
				numsToDelete.append(o)
		numsToDelete = sorted(numsToDelete, reverse=True)
		for x in numsToDelete:
			oxygenCopy.pop(x)
		if len(oxygenCopy) == 1:
			break

	mostCommon [0] * bitCount
	for b in range(bitCount):
		currOnesTally = 0
		numsToDelete = []
		for n in range(len(co2Copy)):
			if co2Copy[n][b] == "1":
				currOnesTally += 1
		if currOnesTally >= (len(co2Copy) - currOnesTally):
			mostCommon[b] = "1"
		else:
			mostCommon[b] = "0"
		for o in range(len(co2Copy)):
			if co2Copy[o][b] == mostCommon[b]:
				numsToDelete.append(o)
		numsToDelete = sorted(numsToDelete, reverse=True)
		for x in numsToDelete:
			co2Copy.pop(x)
		if len(co2Copy) == 1:
			break
	return int(oxygenCopy[0], 2) * int(co2Copy[0], 2)


if __name__ == "__main__":
	print(part1(lines)) # returns 852500
	print(part2(lines)) # return 1007985