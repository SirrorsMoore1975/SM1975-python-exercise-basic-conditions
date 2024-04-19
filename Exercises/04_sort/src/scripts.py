"""
Declare a function sort. Don’t use the built-in sort method.
/**
 * @param {Array<number>} ??? - an array of numbers
 * @returns {Array<number>} a new array with the same elements of the given array in ascending order
 */
 the parameter array shall not be changed

 Quick Sort
 pseudo code
 select the first element as the pivot element
 every thing less than the pivot will be on the left of the pivot element
 every thing bigger than the pivot will be on the right of the pivot element
 recursive leftHandSide and rightHandSide
 return result concatinate leftHandSide, first element and rightHandSide
"""


def sort(array: list) -> list:
    if len(array) <= 1:
        return array
    pivot = array[0]
    leftHandSide = [i for i in array[1:] if i <= pivot]
    rightHandSide = [j for j in array[1:] if j > pivot]
    return sort(leftHandSide) + [pivot] + sort(rightHandSide)



