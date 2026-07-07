class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        n=len(words)
        adj=defaultdict(list)
        chars=set("".join(words))  
        indegree={ch:0 for ch in chars}
        for i in range(n-1):
            w1,w2=words[i],words[i+1]
            mini=min(len(w1),len(w2))
            if len(w1) > len(w2) and w1[:mini] == w2[:mini]:
                return ""
            
            j=0
            while j<mini:
                if w1[j]!=w2[j]:
                    adj[w1[j]].append(w2[j])
                    break
                j+=1
        for node in adj:
            for nei in adj[node]:
                indegree[nei]+=1
        
        q=deque([i for i in indegree if indegree[i]==0])
        res=[]
        while q:
            node=q.popleft()
            res.append(node)
            for nei in adj[node]:
                indegree[nei]-=1
                if indegree[nei]==0:
                    q.append(nei)
        if len(chars)!=len(res):
            return ""
        return "".join(res)           