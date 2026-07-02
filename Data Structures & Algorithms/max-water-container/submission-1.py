class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxi=float('-inf')
        n=len(heights)
        # for i in range(n):
        #     for j in range(i+1,n):
        #         maxi=max((j-i)*min(heights[i],heights[j]),maxi)
        # return maxi
        i=0
        j=n-1
        while i<j:
            maxi=max((j-i)*min(heights[i],heights[j]),maxi)
            if heights[i]>heights[j]:
                j-=1
            else:
                i+=1
        return maxi