from collections import Counter
from typing import List


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        hash = Counter(hand)
        print(hash)
        while hash:
            min_key = min(hash.keys())
            for i in range(groupSize):
                print(hash)
                if hash.get(min_key + i, 0) != 0:
                    hash[min_key + i] = hash.get(min_key + i) - 1
                    if hash.get(min_key + i) == 0:
                        hash.pop(min_key + i)
                else:
                    return False
        return True


hand = [1, 2, 3, 6, 2, 3, 4, 7, 8]
groupSize = 3
hand = [1, 2, 3, 4, 5]
groupSize = 4
res = Solution().isNStraightHand(hand, groupSize)
print(res)
