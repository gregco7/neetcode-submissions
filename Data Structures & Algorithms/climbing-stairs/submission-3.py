class Solution:
    computed = {} # key(number) : climbstairs result
    def climbStairs(self, n: int) -> int:
        if (n < 2):
            return 1
        else:
            if n in self.computed:
                return self.computed[n]
            else:
                computedValue = self.climbStairs(n-1) + self.climbStairs(n-2)
                self.computed[n] = computedValue
                return computedValue
            
        