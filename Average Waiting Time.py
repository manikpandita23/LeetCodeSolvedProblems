class Solution:
    def averageWaitingTime(self, customers):
        total_waiting_time = 0
        current_time = 0
        
        for arrival, time_needed in customers:
            if current_time < arrival:
                current_time = arrival
            current_time += time_needed
            total_waiting_time += current_time - arrival
        
        return total_waiting_time / len(customers)

solution = Solution()

customers1 = [[1,2],[2,5],[4,3]]
print(solution.averageWaitingTime(customers1))  

customers2 = [[5,2],[5,4],[10,3],[20,1]]
print(solution.averageWaitingTime(customers2))  
