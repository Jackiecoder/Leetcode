class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: [-x[0], x[1]])
        sorted_ls = []
        for person in people:
            k = person[1]
            sorted_ls = sorted_ls[:k] + [person] + sorted_ls[k:]
        return sorted_ls
