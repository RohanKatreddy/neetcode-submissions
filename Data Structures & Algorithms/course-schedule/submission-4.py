class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adjacencyMap = defaultdict(list)
        for a, b in prerequisites:
            adjacencyMap[a].append(b)

        visiting = set()
        coursesChecked = set()

        def hasCycle(course):
            if course in coursesChecked: return False
            if course in visiting: return True
            visiting.add(course)

            for preReq in adjacencyMap[course]:
                if hasCycle(preReq): return True
            visiting.remove(course)
            coursesChecked.add(course)
            return False

        return not any(hasCycle(c) for c in range(numCourses))