class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        course_prereqs = {i: [] for i in range(numCourses)}

        for course, prereq in prerequisites:
            course_prereqs[course].append(prereq)
        
        visited = set()

        def dfs(course):
            if course in visited:
                return False
            elif course_prereqs[course] == []:
                return True
            
            visited.add(course)

            for prereq in course_prereqs[course]:
                if not dfs(prereq):
                    return False
            
            visited.remove(course)
            course_prereqs[course] = []

            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True

        