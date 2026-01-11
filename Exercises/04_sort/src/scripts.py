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


def sort(the_list):
    sort_method = ["quick", "bubble", "selection", "insertion", "merge"]
    if len(the_list) <= 1:
        return the_list

    def quick_sort(my_list):
        pivot = my_list[0]
        left_hand_side = [i for i in my_list[1:] if i <= pivot]
        right_hand_side = [j for j in my_list[1:] if j > pivot]
        return sort(left_hand_side) + [pivot] + sort(right_hand_side)

    def bubble_sort(my_list):
        n = len(my_list)
        for i in range(n):
            for j in range(0, n - 1 - i):
                if my_list[j] > my_list[j + 1]:
                    my_list[j], my_list[i] = my_list[j+1], my_list[j]
        return my_list
    
    def selection_sort(my_list):
        return None

    def inserction_sort(my_list):
        return None
    
    def merge_sort(my_list):
        return None
    return None



