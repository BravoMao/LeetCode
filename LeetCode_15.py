class Solution(object):
    def threeSum(self, nums):
        negtiveNum=dict()
        positiveNum=dict()
        hasZero=0
        results=[]
        for num in nums:
            if num>0:
                positiveNum=self.add2CountDict(num,positiveNum)
            elif num<0:
                negtiveNum=self.add2CountDict(num,negtiveNum)
            else:
                hasZero+=1

    #when 0 0 0
        if hasZero>2:
            results.append([0,0,0])

    #when -x 0 x:
        if hasZero>0:
            for key in negtiveNum:
                result=[]
                if positiveNum.__contains__(-key):
                    results.append(self.add3NumToArray(0,key,-key))

    #when -x y z
        for key in negtiveNum:
            results=self.twoSum(key,positiveNum,results)

    #when -x -y z
        for key in positiveNum:
            results=self.twoSum(key,negtiveNum,results)
        return results

    def twoSum(self,target,numdict,results):
        usedSet=set()
        for key in numdict:
            result=[]
            if not usedSet.__contains__(key):
                if numdict.__contains__(-target-key) :
                    if -target-key == key and numdict.get(key)>1:
                        usedSet.add(key)
                        results.append(self.add3NumToArray(target,key,key))
                    elif -target-key != key:
                        usedSet.add(key)
                        usedSet.add(-target-key)
                        results.append(self.add3NumToArray(target,key,-target-key))
        return results

    def add3NumToArray(self,num1,num2,num3):
        result=[]
        result.append(num1)
        result.append(num2)
        result.append(num3)
        return result

    def add2CountDict(self,num,map):
        if map.__contains__(num):
            map[num]+=1
        else:
            map[num]=1
        return map

if __name__ == '__main__':
    solution=Solution()
    S = [-4,3,1]
    print(solution.threeSum(S))