#
# @lc app=leetcode id=232 lang=python
#
# [232] Implement Queue using Stacks
#

# @lc code=start
class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = []
        self.tail = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        if not self.head:
            self.head.append(x)
            while self.head:
                self.head.pop()
            

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end

