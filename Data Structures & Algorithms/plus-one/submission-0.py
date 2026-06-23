class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for num in range(len(digits) - 1, -1, -1):
            digits[num] += 1
            if(digits[num] < 10):
                break
            digits[num] = 0

        if(digits[0] == 0):
            digits[0] = 0
            digits.insert(0, 1)
        
        return digits