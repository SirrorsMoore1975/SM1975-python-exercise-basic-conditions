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

import random

def sort(the_list:list) -> list:
    """
    Sort
    without sort method
    Args:
        the_list(list): unsorted list
    
    Returns:
        return(list): sorted list
    """
    
    def quick_sort(my_list:list) -> list:
        """
        Quick Sort
        1.choose a pivot element
        2.partition the list into two sub-list, depends if they are less or greater that pivot
        3.recursive left hand side and right hand side and apply the above step to sub-list
        
        The usual go to script for sort without internal method. 

        Due to recursive nature, if the pivot is the largest or the smallest number, the sort will iterate in a linear manner instead of dividing the sub-lists into equal parts.

        Time Complexity:
            Best case: 0(N log(N))
            Average case: 0(N long(N))
            Worst caseL 0(N^2)
        
        Space Complexity:
            0(log(N)) : required extra space

        Args:
            my_list(list): a list of unsorted integers
        
        Returns:
            return (list): return a sorted list
        """
        n = len(my_list)
        if n <= 1:
            return my_list
        pivot = my_list[n // 2]
        left_hand_side = [i for i in my_list if i < pivot]
        middle_side = [k for k in my_list if k == pivot]
        right_hand_side = [j for j in my_list if j > pivot]
        return quick_sort(left_hand_side) + middle_side + quick_sort(right_hand_side)

    def bubble_sort(my_list:list)-> list:
        """
        Bubble Sort
        1. start from the first element
        2. compare with the next element
        3. if first element is greater than the next, swap them
        4. move to the next pair, repeat the above comparing steps
        5. continue until the end of the list
        6. where no more swaps are needed, the sort is finished

        flag provided unnecessary sort for already sorted situation

        not efficient for large dataset, good for smaller list and learning about sort 

        Time Complexity:
            Best case: 0(N)
            Average case: 0(N ^2)
            Worst caseL 0(N^2)
        
        Space Complexity:
            0(1) : required no extra space

        Args:

            my_list (list): unsorted list of integers
        
        Returns:

            returns (list): sorted list
        """
        n = len(my_list)
        flag = 0
        # for i in range(n):
        for i in range(n - 1):
            for j in range(0, n - 1 - i):
                if my_list[j] > my_list[j + 1]:
                    # my_list[j], my_list[i] = my_list[j+1], my_list[j]
                    my_list[j], my_list[j+ 1] = my_list[j+1], my_list[j]
                    flag = 1
            if flag == 0:
                break
        return my_list
    
    def selection_sort(my_list):
        """
        Selection Sort
        1. Find the smallest element in the unsorted list
        2. swap the smallest element with the first element
        3. move the boundary between sorted and unsorted portions one element to the right
        4. Repeat the above steps until the list are sorted

        Minimize the number of swaps, make sort much efficient. However, larger data set will required equal sides of steps which make it not efficient for larger list.

        Time Complexity:
            Best case: 0(N^2)
            Average case: 0(N^2)
            Worst caseL 0(N^2)
        
        Space Complexity:
            0(1) : required no extra space

        Args:
            my_list (list): unsorted list

        Returns:

            return (list): sorted list
        """
        n = len(my_list)
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                if my_list[j] < my_list[min_idx]:
                    min_idx = j
            my_list[i], my_list[min_idx] = my_list[min_idx], my_list[i]
        return my_list

    def insertion_sort(my_list):
        """
        Insertion Sort

        1. Assumed the first element is sorted, first select the second element
        2. Compare the current element with the previous elements in the sorted portion
        3. if the current element is smaller, shift the larger element to the right
        4. insert the current element in its correct position in the sorted portion
        5. Move to next unsorted element and repeat the above compare steps until fully sorted

        Efficient for small datasets, it is efficient for partially sorted list. It is an online algorithm, meaning it can sort a list as it receives it.

        Time Complexity:
            Best case: 0(N)
            Average case: 0(N^2)
            Worst caseL 0(N^2)
        
        Space Complexity:
            0(1) : required no extra space

        Args:
            my_list (list): unsorted list
        
        Returns:
            return (list): sorted list
        """
        n = len(my_list)
        for i in range(1, n):
            key = my_list[i]
            j = i - 1
            while j >= 0 and key < my_list[j]:
                my_list[j + 1] = my_list[j]
                j -= 1
            my_list[j + 1] = key
        return my_list
    
    def merge_sort(my_list):
        """
        Merge Sort
        1. Divide unsorted list element into n number of sub-list, each sub-list contain one element. A list of one element is considered sorted.
        2. Repeat merging sub-lists to produce new sorted sub-lists until only one sublist remained. The remained sub-list will be the sorted list

        Time complexity is 0(N log (N)), it is efficient for larger dataset. It required extra space proportional to the size of the input list.

        Time Complexity:
            Best case: 0(N log(N))
            Average case: 0(N log(N))
            Worst caseL 0(N log(N))
        
        Space Complexity:
            0(N) : required extra space

        Args:
            my_list (list): unsorted list

        Returns:
            return (list): sorted list
        """
        n = len(my_list)
        if n > 1:
            mid = n // 2
            left = my_list[:mid]
            right = my_list[mid:]

            merge_sort(left)
            merge_sort(right)

            i = j = k = 0

            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    my_list[k] = left[i]
                    i += 1
                else:
                    my_list[k] = right[j]
                    j += 1
                k += 1

            while i < len(left):
                my_list[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                my_list[k] = right[j]
                j += 1
                k += 1

        return my_list
    
    def select_which_sort(my_list):
        sort_algorithm = ["quick", "bubble", "selection", "insertion", "merge"]
        available = len(sort_algorithm) -1
        the_method = sort_algorithm[random.randint(0,available)]
        #the_method = "quick"
        print(the_method)
        match the_method:
            case "quick":
                return quick_sort(my_list)
            case "bubble":
                return bubble_sort(my_list)
            case "selection":
                return selection_sort(my_list)
            case "insertion":
                return insertion_sort(my_list)
            case "merge":
                return merge_sort(my_list)
            case "_":
                return my_list
    return select_which_sort(the_list)
