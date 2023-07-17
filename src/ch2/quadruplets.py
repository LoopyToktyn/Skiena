from typing import List

def fourSum(nums: List[int], target: int) -> List[List[int]]:
    nums.sort()
    result = []
    for pos in range(len(nums)):
        if pos > 0 and nums[pos] == nums[pos-1]:
            continue # ignore values we've already iterated over!
        for pos2 in range(pos+1,len(nums)):
            if pos2 > pos+1 and nums[pos2] == nums[pos2-1]:
               continue # ignore values we've already iterated over!
            sub_target = target - nums[pos] - nums[pos2]
            sub_result = twoSum(nums[pos2+1:],sub_target)
            for pair in sub_result:
                quad = [nums[pos],nums[pos2],pair[0],pair[1]]
                if quad not in result:
                   result.append(quad)
    return result


def twoSum(nums: List[int], target: int) -> List[List[int]]:
    nums.sort()
    result = []
    for pos,num in enumerate(nums):
        for pair_pos in range(pos+1,len(nums)):
            if pos > 0 and num == nums[pos-1]:
               break # ignore values we've already iterated over!
            if num + nums[pair_pos] == target:
                result.append([num,nums[pair_pos]])
                break # no dupes!
            if num + nums[pair_pos] > target: # no other pair is valid anymore, return immediately
                return result
    return result

def twoSumv2(nums: List[int], target: int) -> List[List[int]]:
    nums.sort()
    start = 0
    end = len(nums) - 1
    result = []
    while start < end:
        if nums[start] + nums[end] == target: 
            result.append([nums[start],nums[end]])
            start += 1
            end -= 1
        if nums[start] + nums[end] > target: 
            end -= 1
            while nums[end] == nums[end+1] and end > start:
                end -= 1
        if nums[start] + nums[end] < target: 
            start += 1
            while nums[start] == nums[start-1] and start < end:
                start += 1
    return result


print(fourSum([-1,0,1,2,-1,-4],-1))


