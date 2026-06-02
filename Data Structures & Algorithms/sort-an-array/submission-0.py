class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.mergesort(nums,0,len(nums)-1)
        return nums
    

    def mergesort(self,a,low,high):
        if low<high:
            mid=low+(high-low)//2
            self.mergesort(a,low,mid)
            self.mergesort(a,mid+1,high)
            self.merge(a,low,mid,high)
    
    def merge(self,a,low,mid,high):
        i,j=low,mid+1
        temp=[]
        while i<=mid and j<=high:
            if a[i]<=a[j]:
                temp.append(a[i])
                i+=1
            else:
                temp.append(a[j])
                j+=1
        while i<=mid:
            temp.append(a[i])
            i+=1
        while j<=high:
            temp.append(a[j])
            j+=1
        for i in range(len(temp)):
            a[low+i]=temp[i]

        