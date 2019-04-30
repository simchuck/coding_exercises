# https://leetcode.com/problems/course-schedule/

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        For 'n' courses, each with possible required prerequisites,
        determine whether it is possible to finish all courses.

        :parameter: numCourses      int     number of courses in the program
        :parameter: prerequisites [[int]]   for ech of the courses

        :returns:   bool    True if all prerequisits can be satisfied
        """

        def next_node(this_node, prerequisites):
            # base case
            # reached end of prerequisites
            if not prerequisites:
                return True

            while prerequisites:
                vector = prerequisites.pop(0)
                if vector[1]:
                    next_node(vector[0], prerequisites)
                else:
                    return False

        return next_node(prerequisites[0][0], prerequisites)


# Submission Detail
# 0 / 42 test cases passed.
#     Status: Runtime Error
