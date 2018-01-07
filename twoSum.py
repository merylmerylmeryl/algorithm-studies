#import ast

class Solution(object):
    def twoSum(self, nums, target):
        '''
        :type nums: List[int]
        :type target: int
        :rtype: List[int]

        Noob solution:
            Look at every combination of numbers O(N^2)

        Any numbers bigger than target can be ignored
        Sort the list and then look at the two ends
        
        '''
        # Make a dictionary mapping nums -> indices
        numDict = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in numDict and numDict[complement] != i:
                return [i, \
                        numDict[complement]]
            numDict[nums[i]] = i

        return numDict
