class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []  # Will store the indices of the days
        
        for i in range(len(temperatures)):
            # Bug 1 Fix: Change >= to > because we need a strictly WARMER temperature
            while stack and temperatures[i] > temperatures[stack[-1]]:
                previous_index = stack.pop()
                answer[previous_index] = i - previous_index
            
            # Bug 2 Fix: Append the current index 'i', not the 'answer' array
            stack.append(i) 
            
        return answer
