class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ui=0
        for i in nums:
            if i!=val:
                nums[ui]=i
                ui+=1
        return ui