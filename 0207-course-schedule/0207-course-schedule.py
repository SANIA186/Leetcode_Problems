class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        
        # Step 1: Build graph
        graph = {i: [] for i in range(numCourses)}
        for a, b in prerequisites:
            graph[a].append(b)

        # Step 2: Track visited state
        visited = [0] * numCourses
        # 0 = not visited
        # 1 = visiting
        # 2 = done (safe)

        # Step 3: DFS function
        def dfs(course):
            # If currently visiting → cycle
            if visited[course] == 1:
                return False

            # If already checked → safe
            if visited[course] == 2:
                return True

            # Mark as visiting
            visited[course] = 1

            # Check all prerequisites
            for nei in graph[course]:
                if not dfs(nei):
                    return False

            # Mark as done
            visited[course] = 2
            return True

        # Step 4: Check all courses
        for i in range(numCourses):
            if not dfs(i):
                return False

        return True