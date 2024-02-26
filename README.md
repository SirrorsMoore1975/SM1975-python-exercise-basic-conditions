# SM1975 python exercise basic conditions
The general proposes of this project is to practice python scripting and passing the test given to each python function under the test driven development method (using `pytest`)

# Index for the functions
(under constructions)

## How to run this project

the folder structure for each function should be like so:- 
```
Exercises
    |---isRainbow
        |--- src
        |   |--- __init__.py
        |   |--- scripts.py
        |
        |--- test
            |--- __init__.py
            |--- conftest.py
            |--- pytest.ini
            |--- test_isRainbow
                |--- __inti__.py
                |--- scripts_test.py
```
Where:
- `__init__.py` located inside `src`, `test` and `test_{function_name}` folders are empty files that allow python to locate the `scripts.py` and `scripts_test.py`.
- `conftest.py` and `pytest.ini` located inside `test` folder are empty files that are necessary for pytest to work.

You should categories the function inside a folder and name the folder the function name.

## Create the function inside scripts.py
Each function should be inside `src/scripts.py`:
```
{function_name}/src/scripts.py 
```
__Note:__ `{function_name}` should be the function name of your scripts

## Create the test inside scripts_test.py
The test scripts for the function should be inside:
```
{function_name}/test/test_{function_name}/scripts_test.py
```
__Note:__ `{function_name}` should be the function name of your scripts


## Run the project inside venv
1. Pick a location in your disk drive to clone this project
1. Navigate to the directory
1. Start the project by creating the virtual environment:-
```
python -m venv env
```
For Linux or Unix like system, run the following to start the environment:-
```
source env/bin/activate
```
For Windows, run the following to start the environment:-
```
env\Scripts\activate.bat
```
## Install project dependencies
Install project dependencies:-
```
pip install package1 package2
```
(We needed pytest, replace package with `pytest`)

## Install dependencies from a requirements.txt file
If you are cloning the project from source, install dependencies from a requirements.txt file:-
```
pip install -r requirements.txt
```
## The requirements.txt file
The `requirements.txt` can be generated or updated by running:-
```
pip freeze -> requirements.txt
```

Be sure to locate `requirements.txt` at the root location of the project
## Deactivate virutal environment
You can deactivate the virtual environment by running the following:-
```
deactivate
```

## Test you function
1. Relocate your location to the function name folder.
1. Running the following command should check if the scripted function passed the scripts_test test:-
```
(venv)$ python -m pytest test
```
__Note:__ make sure `scripts_test.py` import the function from the correct path:-

```py
from src.scripts import isRainbow
```

# Sources
For test driven development in python, read the following:
[Modern Test-Driven Development in Python](https://testdriven.io/blog/modern-tdd/)