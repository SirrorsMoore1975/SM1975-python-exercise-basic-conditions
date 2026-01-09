# addTogether

## Introduction

The function that adding two or more array's element together, for example, if we have the following, when we fetch the parameters to the addTogether function, it should return a sum result:

```py

a = [1,2,3]
b = [2,3,4]

print(addTogether(a,b)) 
# should print [3,5,7]

```

## Basic Requirement

`test_addTogether`

past the test for adding two equal sized array and get the expected result to pass the test.

```py
# 1
x = [1,2,3]
y = [4,5,6]
print(addTogether(x,y))
# expected output: [5,7,9]
```

```py
#2
x = [1,2,3]
y = [7,8,9]
print(addTogether(x,y))
# expected output: [8,10,12]
```

## Advanced Requirement

`test_addTogether_Advanced`

Alter the `addTogether` function so that the following tests are also passed. The arrays are at different length.

```py
#3 
x = [1]
y = [4,5,6]
print(addTogether(x,y))
# expected : [5,5,6]
```

```py
#4
x = [1,5,6]
y = [4]
print(addTogether(x,y))
# expected : [5,5,6]
```

## Intermediate Requirement

alter the function `addTogether` so that it can add multiple lists with different length and also passed the given test.

```py
addTogether(*x)
```
