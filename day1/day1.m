% Reference to documentation on "readcell" function
% https://www.mathworks.com/help/matlab/ref/readcell.html
nums = readcell('day1data.txt');
incrCounterPt1 = 0;
% Part 1
for i=2:length(nums)
    if nums{i} > nums{i-1}
        incrCounterPt1 = incrCounterPt1 + 1;
    end
end

% Part 2
incrCounterPt2 = 0;
for i=2:length(nums)
    if i < (length(nums)-1)
        currSum = nums{i} + nums{i+1} + nums{i+2};
        prevSum = nums{i-1} + nums{i} + nums{i+1};
        if currSum > prevSum
            incrCounterPt2 = incrCounterPt2 + 1;
        end
    end
end

fprintf('The answer to part 1 is %d\n', incrCounterPt1);
fprintf('The answer to part 2 is %d\n', incrCounterPt2);