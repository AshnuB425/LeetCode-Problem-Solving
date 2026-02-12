class Solution:
    def mergeAdjacent(self, nums: List[int]) -> List[int]:
        st=[]
        for i in range(len(nums)):
            st.append(nums[i])
            while len(st)>=2 and st[-1]==st[-2]:
                top=st[-1]
                st.pop()
                st.pop()
                st.append(2*top)
        return st
