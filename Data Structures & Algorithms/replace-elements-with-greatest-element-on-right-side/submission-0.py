class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if len(arr) <= 1:
            return [-1]
        
        
        right_pointer = len(arr) - 1
        cur_max = arr[right_pointer]

        while right_pointer >= 0:
            if arr[right_pointer] > cur_max:
                new_max = arr[right_pointer]
                arr[right_pointer] = cur_max
                cur_max = new_max
            else:
                arr[right_pointer] = cur_max
            right_pointer -= 1
        
        arr[-1] = -1

        return arr
