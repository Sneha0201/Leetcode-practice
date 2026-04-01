class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        robots = sorted(zip(positions, healths, directions, range(len(positions))))
        stack = []
        health = healths[:]
        for pos, h, d, i in robots:
            if d == "R":
                stack.append(i)
            else:
                while stack and health[i] > 0:
                    j = stack[-1]
                    if health[j] < health[i]:
                        stack.pop()
                        health[i] -= 1
                        health[j] = 0
                    elif health[j] > health[i]:
                        health[j] -= 1
                        health[i] = 0
                        break
                    else:
                        health[j] = 0
                        health[i] = 0
                        stack.pop()
                        break
        res = []
        for i in range(len(health)):
            if health[i] > 0:
                res.append(health[i])
        return res