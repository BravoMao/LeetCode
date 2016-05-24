class Solution(object):
    def intersection(self, nums1, nums2):
        set_nums1=set()
        result=set()
        rtype=[]
        for num1 in nums1:
            if not set_nums1.__contains__(num1):
                set_nums1.add(num1)

        for num2 in nums2:
            if(set_nums1.__contains__(num2)):
                if(not result.__contains__(num2)):
                    result.add(num2)
        rtype=list(result)
        return rtype

if __name__ == '__main__':
    solution=Solution()
    nums1=[1, 2, 2, 1]
    nums2=[2, 2]
    print(solution.intersection(nums1,nums2))

