# Calculation
In this exercise, you will create a function `calculation` which take in three (3) parameters:-

```py
"""
A list with a given value and do calculation according to the given calculation sign and return a list 
 @params {sign} <string> { 
    \t "add" 
    \t "subtract" 
    \t "multiply" 
    \t "divide" 
    \t "getRemainder" 
    } 
    : the sign that a list of element will be interacting with the value 

 @params {x} <list> a list of numerical calculation that the function will try to interact with

 @param {value} <int> a number value that is going to apply to the list element
 
 @returns {list} return the list that has applied the given input parameters calculation

 """

```

For example: if we are given a list `[1,2,3,4]`, with sign `add` and a value `6`, `calculation` function should return a list `[7,8,9,10]`

However, as any number dividing it by zero leads to calculation error or returning `Infinite`, we want the function to return `0` when this happened.