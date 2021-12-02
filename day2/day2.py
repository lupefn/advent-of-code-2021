with open("day2data.txt") as file:
	lines = file.read().split("\n")

def part1(inst):
	horizontalPos = 0
	depth = 0
	for i in inst:
		splitInst = i.split(" ")
		if splitInst[0] == "forward":
			horizontalPos += int(splitInst[1])
		elif splitInst[0] == "down":
			depth += int(splitInst[1])
		else:
			depth -= int(splitInst[1])
	return horizontalPos * depth

def part2(inst):
	horizontalPos = 0
	depth = 0
	aim = 0
	for i in inst:
		splitInst = i.split(" ")
		if splitInst[0] == "forward":
			horizontalPos += int(splitInst[1]) 
			depth += (aim * int(splitInst[1]))
		elif splitInst[0] == "down":
			aim += int(splitInst[1])
		else:
			aim -= int(splitInst[1])
	return horizontalPos * depth

if __name__ == "__main__":
	print(part1(lines)) #prints 2187380
	print(part2(lines)) #prints 2086357770