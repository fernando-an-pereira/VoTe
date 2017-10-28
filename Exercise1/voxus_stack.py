'''
VoxusStack class module
'''

class VoxusStack(object):
    '''
    Efficient implementation of a queue
    with push, pop and min methods
    '''

    def __init__(self):
        self.main_stack = []
        self.min_stack = []

    def push(self, val):
        '''Add val to the end of the queue'''

        self.main_stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self):
        '''Remove and return the last element of the queue'''

        val = self.main_stack.pop()
        if val == self.min_stack[-1]:
            self.min_stack.pop()
        return val

    def min(self):
        '''Return the smallest item in the queue'''

        if self.min_stack:
            return self.min_stack[-1]
        return None
