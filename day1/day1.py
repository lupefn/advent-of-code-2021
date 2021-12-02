# reading in file with data
with open ("day1data.txt") as file:
    lines = file.read().split("\n")

def part1(nums):
    incrCount = 0
    for i in range(1, len(nums)):
        currentNum = int(nums[i])
        prevNum = int(nums[i-1])
        if currentNum > prevNum:
            incrCount += 1
    return incrCount

def part2(nums):
    incrCount = 0
    for i in range(1, len(nums)):
        if (i+2) < len(nums):
            currSum = int(nums[i]) + int(nums[i+1]) + int(nums[i+2])
            prevSum = int(nums[i-1]) + int(nums[i]) + int(nums[i+1])
            if currSum > prevSum:
                incrCount += 1
    return incrCount

if __name__ == "__main__":
    print(part1(lines))
    print(part2(lines))