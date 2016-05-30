class Solution(object):
    def increasingTriplet(self, nums):
        min,mid,max=None,None,None
        for index in range(0,len(nums))[::-1]:
            if(nums[index]>max):
                max=nums[index]
                mid=None
                continue
            if(nums[index]==max):
                continue
            if(nums[index]>=mid):
                mid=nums[index]
                continue
            if(nums[index]>min):
                return True

        return False


if __name__ == '__main__':
    nums=[1,1,-2,6]
    solution=Solution()
    print(solution.increasingTriplet(nums))