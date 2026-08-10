class Solution(object):
    def getImportance(self, employees, id):

        # Map employee id to employee object
        emp_map = {emp.id: emp for emp in employees}

        queue = [id]
        total = 0

        while queue:
            emp_id = queue.pop(0)
            emp = emp_map[emp_id]

            total += emp.importance

            for sub in emp.subordinates:
                queue.append(sub)

        return total