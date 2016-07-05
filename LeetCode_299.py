class Solution(object):
    def getHint(self, secret, guess):
        nums_dict=dict()
        bulls,cows=0,0
        for index in range(len(secret)):
            nums_dict[secret[index:index+1]]=nums_dict.get(secret[index:index+1],0)+1
        for index in range(len(guess)):
            if(guess[index:index+1]==secret[index:index+1]):
                nums_dict[guess[index:index+1]]-=1
                bulls+=1
            elif(nums_dict.__contains__(guess[index:index+1])):
                if(nums_dict[guess[index:index+1]]>0):
                    cows+=1
                    nums_dict[guess[index:index+1]]-=1
        for key in nums_dict:
            if(nums_dict[key]<0):
                cows+=nums_dict[key]
        result=str(bulls)+"A"+str(cows)+"B"
        return result





if __name__ == '__main__':
    secret="1122"
    guess="1222"
    solution=Solution()
    print(solution.getHint(secret,guess))