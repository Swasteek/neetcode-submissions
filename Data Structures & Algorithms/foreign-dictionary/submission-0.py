from collections import defaultdict, deque
from typing import List

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = defaultdict(list)

        # all unique chars
        chars = set("".join(words))

        # build graph
        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]

            minLen = min(len(w1), len(w2))

            # invalid case
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""

            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].append(w2[j])
                    break

        # indegree
        indegree = {ch: 0 for ch in chars}

        for u in adj:
            for v in adj[u]:
                indegree[v] += 1

        # topo sort
        q = deque()

        for ch in indegree:
            if indegree[ch] == 0:
                q.append(ch)

        res = []

        while q:
            node = q.popleft()
            res.append(node)

            for nei in adj[node]:
                indegree[nei] -= 1

                if indegree[nei] == 0:
                    q.append(nei)

        # cycle check
        if len(res) != len(chars):
            return ""

        return "".join(res)