from collections import defaultdict
# 215개중 155개 통과, Memory Limit Exceeded
class Solution:
    minlen = -1
    def pancakeSort(self, arr: list) -> list:
        cache = defaultdict()
        def temp(ar:list, path:list, visited:set):
            if self.minlen > 0 and len(path) >= self.minlen : 
                del visited
                return
            if tuple(ar) not in visited:
                visited.add(tuple(ar))
            else:
                del visited
                return
            if(sorted(ar)==ar):
                if self.minlen <0 or self.minlen > len(path):
                    self.minlen = len(path)
                del visited
                return path
            else:
                ans = []
                for i in range(2,len(ar)+1):
                    cpar = ar[:i].copy()
                    cpar.reverse()
                    param = cpar + ar[i:]
                    key = tuple(path+[i])
                    if key in cache:
                        tmp = cache.get(key)
                    else:
                        tmp =  temp(param, path+[i], visited.copy())
                        cache.update({key: tmp})
                    if isinstance(tmp, list):
                        ans.append(tmp)
                del visited
                return sorted(ans, key=lambda x: -len(x)).pop() if len(ans)>0 else None
        if len(arr) >1:
            hist = set()
            ans = temp(arr,[], hist)
        else:
            ans = []
        return ans
sol = Solution()
# ans = sol.pancakeSort([3,2,4,1])
ans = sol.pancakeSort([10,5,1,6,3,8,2,4,7,9])
print(ans)
# 2,3,4,1
# 4,3,2,1

# 1,4,2,3
# 2,4,1,3
# 4,2,1,3