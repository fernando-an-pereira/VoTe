'''
TestVoxusStack class module
'''

import pytest

from voxus_stack import VoxusStack

class TestVoxusStack(object):
    '''
    A test class for the VoxusStack
    '''

    def test_simple(self):
        stack = VoxusStack()
        stack.push(9)
        assert stack.min() == 9
        assert stack.pop() == 9

    def test_push_desc(self):
        stack = VoxusStack()
        stack.push(9)
        assert stack.min() == 9
        stack.push(8)
        assert stack.min() == 8
        stack.push(7)
        assert stack.min() == 7

    def test_push_asc(self):
        stack = VoxusStack()
        stack.push(9)
        assert stack.min() == 9
        stack.push(10)
        assert stack.min() == 9
        stack.push(11)
        assert stack.min() == 9

    def test_push_random(self):
        stack = VoxusStack()
        stack.push(9)
        assert stack.min() == 9
        stack.push(13)
        assert stack.min() == 9
        stack.push(5)
        assert stack.min() == 5
        stack.push(18)
        assert stack.min() == 5
        stack.push(1)
        assert stack.min() == 1

    def test_push_pop_min(self):
        stack = VoxusStack()
        stack.push(9)
        assert stack.min() == 9
        stack.push(13)
        assert stack.min() == 9
        stack.push(5)
        assert stack.min() == 5
        assert stack.pop() == 5
        assert stack.min() == 9
        stack.push(18)
        assert stack.min() == 9
        stack.push(1)
        assert stack.min() == 1
        assert stack.pop() == 1
        assert stack.min() == 9
        assert stack.pop() == 18
        assert stack.min() == 9
        assert stack.pop() == 13
        assert stack.min() == 9
        assert stack.pop() == 9
    
    def test_pop_exception(self):
        stack = VoxusStack()
        stack.push(9)
        assert stack.min() == 9
        assert stack.pop() == 9
        with pytest.raises(Exception) as excinfo:   
            stack.pop()
        assert excinfo.value.message == 'Trying to pop from empty stack' 

    def test_min_exception(self):
        stack = VoxusStack()
        stack.push(9)
        assert stack.min() == 9
        assert stack.pop() == 9
        with pytest.raises(Exception) as excinfo:   
            stack.min()
        assert excinfo.value.message == 'Trying to return min value from empty stack' 
