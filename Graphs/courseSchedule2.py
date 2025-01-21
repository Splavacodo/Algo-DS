from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) ->list[int]:
        indegrees = [0 for _ in range(numCourses)]
        course_prereqs = [[] for _ in range(numCourses)]

        for course, prereq in prerequisites:
            indegrees[prereq] += 1
            course_prereqs[course].append(prereq)
        
        queue = deque()
        
        for course in range(numCourses):
            if indegrees[course] == 0:
                queue.append(course)
        
        ordered_courses = []
        finished = 0

        while queue:
            course = queue.popleft()
            ordered_courses.append(course)
            finished += 1

            for other_course in course_prereqs[course]:
                indegrees[other_course] -= 1

                if indegrees[other_course] == 0:
                    queue.append(other_course)
        
        return ordered_courses[::-1] if numCourses == finished else []