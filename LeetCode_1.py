class Solution(object):
    def twoSum(self, nums, target):
        indiceDict=dict()
        countDict=dict()
        i=0
        for num in nums:
            indiceDict[num]=i
            i+=1

        j=0
        result=[]
        for num in nums:
            if indiceDict.__contains__(target-num) and indiceDict.get(target-num)!=j:
                print(num)
                result.append(j)
                result.append(indiceDict.get(target-num))
                return result
            j+=1
        return result

if __name__ == '__main__':
    nums=[3,2,4]
    target=6
    s=Solution()
    print(s.twoSum(nums,target))