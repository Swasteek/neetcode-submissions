class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj=defaultdict(list)
        indegree=[0]*numCourses
        for i,j in prerequisites:
            adj[j].append(i)
            indegree[i]+=1
        q=deque()
        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)
        cnt=0
        res=[]
        while q:
            node=q.popleft()
            cnt+=1
            res.append(node)
            for nei in adj[node]:
                indegree[nei]-=1
                if indegree[nei]==0:
                    q.append(nei)
        return res if cnt==numCourses else []