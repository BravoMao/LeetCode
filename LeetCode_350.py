class Solution(object):
    @staticmethod
    def intersect(self, nums1, nums2):
        result=[]
        nums1_dict=dict()
        for i in nums1:
            nums1_dict[i]=nums1_dict.get(i,0)+1

        for j in nums2:
            if nums1_dict.get(j,0)>0:
                result.append(j)
                nums1_dict[j]=nums1_dict.get(j)-1

        return result

if __name__ == '__main__':
    nums1=[1, 2, 2, 1]
    nums2=[2, 2]
    #solution=Solution()
    result=Solution.intersect(Solution,nums1,nums2)
    print(result)