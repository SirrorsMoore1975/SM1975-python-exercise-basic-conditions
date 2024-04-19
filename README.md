# SM1975 python exercise basic conditions
The general purpose of this project is to practice python scripting and passing the test given to each python function under the test driven development method (using `pytest`)

# Index for the functions
(under constructions)

## How to create a new exercise with viable pytest ready

the Exercises folder structure for each function should be like so:- 
```
Exercises
    |---03_isRainbow
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

### Use the crtx shell script at bin
`crtx.sh` is just a short form of <u>cr</u>ea<u>t</u>e e<u>x</u>ercise. Executing the script will automatic add a new exercise function under the `/Exercises` folder. You can either create the sturcture mentioned above all by yourself or execute the `crtx.sh` at the `/bin` folder.

#### Usage of crtx
Run the `crtx.sh` inside bin folder, follow one of the below syntax to run the shell script:-
```bash
./crtx.sh {function_name} 
sh crtx.sh {function_name}
bash crtx.sh {function_name}
```
The script can detect whether the `function_name` has already been used or not. If the `function_name` has been used, it will not create the exercise and end the script. An empty `function_name` will not work either.

For example:
```bash
sh crtx.sh isRainbow
```
`isRainbow` will be added under `/Exercises`, you should then script your `isRainbow` function under `/Exercise/isRainbow/src/scripts.py` and write the test script at `/Exercise/isRainbow/test/test_isRainbow/scripts_test.py`. Execute pytest inside `/isRainbow` folder will show the result of running the script and the test script.

__NB:__ In the time of writing this, `isRainbow` already existed, so the script will exit without creating `isRainbow`.

#### Optional: export to virtual environment PATH
 or alternatively, you can export the bin folder location to the virtual environment path by exporting the `PATH` of the bin folder in your local `env/bin/activate` file, add the following line to the file:-
```bash
export PATH="$PATH:./../bin"
```
### Write your exercise script and test script
#### Create the function inside scripts.py
Each function should be inside `src/scripts.py`:
```
{function_name}/src/scripts.py 
```
__Note:__ `{function_name}` should be the function name of your scripts



## Create the test inside scripts_test.py
The test scripts for the function should be inside:
```
./Exercise/{function_name}/test/test_{function_name}/scripts_test.py
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
If you are cloning the project from source, install dependencies from a `requirements.txt` file:-
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
1. Relocate your location to the function name folder. Make sure you are in the right location: `(env) /path/to/your/exercises/function$ `
1. Running the following command should check if the scripted function passed the `scripts_test.py` test:-
```
python -m pytest test
```
__Note:__ make sure and check your `scripts_test.py` file has imported the function from the correct path:-

```py
from src.scripts import isRainbow
```
<div style="margin-left:60px;">^^^^^^^^^^</div>

# Sources
For test driven development in python, read the following:
[Modern Test-Driven Development in Python](https://testdriven.io/blog/modern-tdd/)
