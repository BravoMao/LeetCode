class Solution(object):
    def firstBadVersion(self, n):
        first,last=1,n
        if n==1:
            if isBadVersion(1):
                return 1

        while(first<last):
            mid=(first+last)/2
            if(isBadVersion(mid)):
                if(not isBadVersion(mid-1)):
                    return mid
                else:
                    last=mid-1
            else:
                if(isBadVersion(mid+1)):
                    return mid+1
                else:
                    first=mid+1
        return 1