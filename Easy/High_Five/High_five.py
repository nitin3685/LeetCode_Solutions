class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:

        from collections import defaultdict
        stud_dict = defaultdict(list)
        for student in items:
            stud_dict[student[0]].append(student[1])
        res = list()
        for student,scores in stud_dict.items():
            average = sum(sorted(scores)[-5:])//5
            res.append([student,average])
        return res
