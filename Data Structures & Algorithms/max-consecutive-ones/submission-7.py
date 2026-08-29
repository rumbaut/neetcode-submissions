class Solution:
    #[1,1,1,0,1] index = 1; n = 1; n - 1 = 1; acc = 2, max_cons = 0
    #[ 1, 1, 1, 0, 1] index = 2; n = 1; n -1 = 1; acc = 3 max_cons = 0
    #[ 1, 1 , 1, 0, 1] index = 3; n = 0; n - 1 = 1; acc = 1; max_cons = 3
    #[1,1,1,0,1] index = 4; n = 1; n - 1 = 0; acc = 1; max_cons = 3 
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        current_count = 0
        max_consecutives = 0
        for n in nums:
            if n == 1:
                current_count += 1
            else:
                max_consecutives = max(max_consecutives, current_count)
                current_count = 0
                
        return max(current_count, max_consecutives)
        