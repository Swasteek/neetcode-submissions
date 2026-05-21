class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        st=set(wordList)
        if endWord not in st:
            return 0
        q=deque([(beginWord,1)])
        alphabets='abcdefghijklmnopqrstuvwxyz'
        while q:
            word,step=q.popleft()
            if word==endWord:
                return step
            for i in range(len(word)):
                for j in alphabets:
                    new=word[:i]+j+word[i+1:]
                    if new!=word and new in st:
                        q.append((new,step+1))
                        st.remove(new)
        return 0

            