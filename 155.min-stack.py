#
# @lc app=leetcode id=155 lang=python
#
# [155] Min Stack
#

# @lc code=start

# Solution 2 : two stack
class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minStack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        
        if not self.minStack or x <= self.minStack[-1]:
            self.minStack.append(x)

    def pop(self):
        """
        :rtype: None
        """
        if self.stack[-1] == self.minStack[-1]:
            self.minStack.pop()
        self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.minStack[-1]
        
    """
    # solution 1 : one stack
    def __init__(self):
        
        # initialize your data structure here.
        
        self.stack = []

    def push(self, x):
        
        #:type x: int
        #:rtype: None
        
        if not self.stack:
            self.stack.append((x, x))
            return 

        current_min = self.stack[-1][1]
        self.stack.append((x, min(x, current_min)))

    def pop(self):
        
        #:rtype: None
        
        self.stack.pop()

    def top(self):
        
        #:rtype: int
        
        return self.stack[-1][0]

    def getMin(self):
        
        #:rtype: int
        
        return self.stack[-1][1]
    """

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

