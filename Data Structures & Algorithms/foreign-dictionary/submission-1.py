class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj=defaultdict(list)
        chars=set("".join(words))   

        for i in range(len(words)-1):
            w1=words[i]
            w2=words[i+1]
            n=min(len(w1),len(w2))

            if len(w1)>len(w2) and w1[:n]==w2[:n]:
                return ""
            for j in range(n):
                if w1[j]!=w2[j]:
                    adj[w1[j]].append(w2[j])
                    break
        
        q=deque()
        indegree={ch:0 for ch in chars}
        for node in adj:
            for nei in adj[node]:
                indegree[nei]+=1
        for i in indegree:
            if indegree[i]==0:
                q.append(i)
        res=[]
        while q:
            node=q.popleft()
            res.append(node)
            for nei in adj[node]:
                indegree[nei]-=1
                if indegree[nei]==0:
                    q.append(nei)
        if len(res) != len(chars):
            return ""
        return "".join(res)