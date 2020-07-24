def coinChange(self, coins, amount: int) -> int:
    memory = dict()
    def helper(temp):
        if temp in memory.keys():
            return memory[temp]
        re = float('inf')
        if temp < 0:
            return -1
        if temp == 0:
            return 0
        for i in coins:
            subproblem = helper(temp - i)
            if subproblem == -1:
                continue
            re = min(subproblem + 1, re)
        memory[temp] = re if re != float('inf') else -1
        return memory[temp]
    return helper(amount)