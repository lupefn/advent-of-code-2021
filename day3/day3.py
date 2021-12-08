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

	oxygenNum = findRatings(oxygenCopy, 1, bitCount)
	co2Num = findRatings(co2Copy, 0, bitCount)
	return oxygenNum * co2Num

def findRatings(report, oxyFlag, count):
	mostCommon = [0] * count
	for b in range(count):
		currOnesTally = 0
		numsToDelete = []
		for n in range(len(report)):
			if report[n][b] == "1":
				currOnesTally += 1
		if currOnesTally >= (len(report) - currOnesTally):
			mostCommon[b] = "1"
		else:
			mostCommon[b] = "0"
		for o in range(len(report)):
			if oxyFlag:
				if report[o][b] != mostCommon[b]:
					numsToDelete.append(o)
			else:
				if report[o][b] == mostCommon[b]:
					numsToDelete.append(o)
		numsToDelete = sorted(numsToDelete, reverse=True)
		for x in numsToDelete:
			report.pop(x)
		if len(report) == 1:
			break
	return int(report[0], 2)

if __name__ == "__main__":
	print(part1(lines)) # returns 852500
	print(part2(lines)) # return 1007985