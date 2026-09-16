class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        A=[]
        for i, num in enumerate(nums):
            A.append([num,i])
        A.sort()
        print(A)
       

        i=0
        j=len(A)-1
      

        while i<j:

            result = A[i][0]+A[j][0]
            print(result)
            print(i,j)
           

            if result == target:
                return [min(A[i][1],A[j][1]), max(A[i][1],A[j][1])]
            elif result < target:
                i+=1
            else:
                j-=1
        return []

        