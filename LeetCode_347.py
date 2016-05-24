import heapq
import collections
class Solution(object):
    def topKFrequent(self,nums,k):
        dict_nums=dict()
        result=[]
        for num in nums:
            dict_nums[num]=dict_nums.get(num,0)+1
        mc=collections.Counter(dict_nums).most_common(k)
        result=map(lambda x: x[0], mc)
        return result

if __name__ == '__main__':
    solution=Solution()
    nums=[1,1,1,2,2,3,5,5,5]
    print(solution.topKFrequent(nums,2))
