class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree=[0]*numCourses
        adj=defaultdict(list)
        for i,j in prerequisites:
            adj[j].append(i)
            indegree[i]+=1

        q=deque([i for i in range(numCourses) if indegree[i]==0])
        res=[]
        while q:
            node=q.popleft()
            res.append(node)
            for nei in adj[node]:
                indegree[nei]-=1
                if indegree[nei]==0:
                    q.append(nei)

        return len(res)==numCourses