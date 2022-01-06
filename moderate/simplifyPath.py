from collections import Counter
from typing import List


class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        names = path.split('/')
        for i in names:
            if i == '..':
                if stack:
                    stack.pop()
            elif i != '.' and i:
                stack.append(i)
        return '/' + '/'.join(stack)


path = '/home/'
path = '/../'
res = Solution().simplifyPath(path)
print(res)
