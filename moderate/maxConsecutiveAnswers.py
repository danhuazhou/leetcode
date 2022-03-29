class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        def maxConsecutiveChar(ch: str) -> int:
            ans, left, sum = 0 ,0 ,0
            n = len(answerKey)
            for right in range(n):
                print(left, right, sum)
                # 字符不为变更字符 计数加一
                if answerKey[right] != ch:
                    sum += 1
                # 计数超过可变更次数
                while sum > k:
                    # 左边字符不为变更字符时计数减一
                    sum -= answerKey[left] != ch
                    # 左边界向右移动
                    left += 1
                ans = max(ans, right - left + 1)
            return ans
        return max(maxConsecutiveChar('T'), maxConsecutiveChar('F'))
answerKey = "TTFFTTFTT"
k = 2
obj = Solution()
res = obj.maxConsecutiveAnswers(answerKey, k)
print(res)