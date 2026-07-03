class Solution:
    def isValid(self, s: str) -> bool:
        mpp={
            "]":"[",
            "}":"{",
            ")":"("
        }
        st=[]
        for i in s:
            if i in "{([":
                st.append(i)
            else:
                if st and mpp[i]==st[-1]:
                    st.pop()
                else:
                    return False
        return len(st)==0