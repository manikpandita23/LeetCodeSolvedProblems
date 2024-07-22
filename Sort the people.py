from typing import List
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        people = list(zip(names, heights))
        people.sort(key=lambda x: x[1], reverse=True)
        sorted_names = [person[0] for person in people]
        return sorted_names
sol=Solution()
names1 = ["Mary", "John", "Emma"]
heights1 = [180, 165, 170]
print(sol.sortPeople(names1, heights1))
names2 = ["Alice", "Bob", "Bob"]
heights2 = [155, 185, 150]
print(sol.sortPeople(names2, heights2))
        
