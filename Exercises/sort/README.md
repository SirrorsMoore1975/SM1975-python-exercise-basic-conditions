# SORT
There are many ways to sort a numerical list. 
Without using build-in method, write a function to sort the given list, the input array must not be altered.
Tasks:-
- [ ] write a sort function without using build-in method
- [ ] the function does not change the input list
```py
import pytest
from scripts import sort

@pytest.mark.parametrize("array,expected",[
    ([5, 4, 3, 2, 1],[1, 2, 3, 4, 5]),
    ([3, 5, 6, 2, 1, 4],[1, 2, 3, 4, 5, 6]),
    ([1, 2, 2, 3, 3, 3, 4, 3 , 3, 3, 2, 2, 1],[1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4]),
    ([20, 1, 1, 2, 2, 3, 3, 5, 5, 4, 20, 4, 5],[1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 5, 20, 20]),
    ([ 20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5 ],[-2, -2, -1, -1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 5, 20, 20])
])

def test_sort(array,expected):
    initalArray = array
    sorted = sort(array)
    print(f"Test: sort({array})")
    print(f"actual:{sort(array)}")
    print(f"Should return: {expected}")
    assert sorted == expected

    print(f"Test: the input array should not be changed")
    print(f"actual: {array}")
    print(f"expected: {initalArray}")
    assert array == initalArray
 ```