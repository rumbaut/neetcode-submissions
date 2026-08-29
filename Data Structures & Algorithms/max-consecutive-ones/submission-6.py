class Solution:
    #[1,1,1,0,1] index = 1; n = 1; n - 1 = 1; acc = 2, max_cons = 0
    #[ 1, 1, 1, 0, 1] index = 2; n = 1; n -1 = 1; acc = 3 max_cons = 0
    #[ 1, 1 , 1, 0, 1] index = 3; n = 0; n - 1 = 1; acc = 1; max_cons = 3
    #[1,1,1,0,1] index = 4; n = 1; n - 1 = 0; acc = 1; max_cons = 3 
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if len(nums) == 1: return 1 if nums[0] == 1 else 0
       
        max_cons= 0;
        prev = None
        current = None
        acc = 1 if nums[0] == 1 and nums[1] == 1 else 0
        index = 1

        while index < len(nums):
            prev = nums[index - 1]
            current = nums[index]
            if prev == current and current == 1:
                acc += 1;
            else:
                max_cons = max(max_cons, acc)
                acc = 1 if current == 1 else 0
            index += 1
        
        max_cons = max(max_cons, acc)

        
     
            
                
        return max_cons
        