#
# Given an array of integers, return the indices of the two numbers that when added will become the specified target 
# Assume that each input will have only one answer so no need to worry about checking for multiple solutions 
# 
print("Two Sum Program")

# actual two sum function
def twoSum(nums, target):
        """
        The list of numbers is mapped to indexes, then check if target - num is in the list num_to_index we return other wise we keep adding to num_to_index 
        An empty value is returned if target - num is not present in the entire list nums
        """
        
        num_to_index = {} # key is actually the number while value is index in the nums array
        for i, num in enumerate(nums):
            if target - num in num_to_index:
                return [num_to_index[target - num] , i]
            num_to_index[num] = i
            
        return [] # no sum

# example to test the funcion twoSum
list = [1,2,2,4,7];
tget = 8; 
print(twoSum(list, tget));
        
