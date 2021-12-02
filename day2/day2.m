instruct = readcell('day2data.txt');
% vars for pt 1
horizPosPt1 = 0;
depthPt1 = 0;
% vars for pt 2
horizPosPt2 = 0;
depthPt2 = 0;
aim = 0;

for i=1:length(instruct)
    if strcmp(instruct{i,1}, 'forward')
        horizPosPt1 = horizPosPt1 + instruct{i,2};
    elseif strcmp(instruct{i,1}, 'down')
        depthPt1 = depthPt1 + instruct{i,2};
    else
        depthPt1 = depthPt1 - instruct{i,2};
    end
end

for i=1:length(instruct)
    if strcmp(instruct{i,1}, 'forward')
        horizPosPt2 = horizPosPt2 + instruct{i,2};
        depthPt2 = depthPt2 + (aim * instruct{i,2});
    elseif strcmp(instruct{i,1}, 'down')
        aim = aim + instruct{i,2};
    else
        aim = aim - instruct{i,2};
    end
end

fprintf('The answer to part 1 is %d\n', (horizPosPt1 * depthPt1));
fprintf('The answer to part 1 is %d\n', (horizPosPt2 * depthPt2));