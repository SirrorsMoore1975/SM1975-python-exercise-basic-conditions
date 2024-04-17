#!/bin/bash

# NB: execute crtx.sh using ./crtx.sh
# Do not use space, IFS is the default behaviour

if [ -z "$1" ]; then
    echo "Please provide a project name after ./crtx.sh"
    echo "Exit script without create any directories or files"
    exit 1
fi

current_path=$(pwd)
folder_path="./../Exercises"
project_name="$1"
directories=$(find "$folder_path" -maxdepth 1 -type d)
num_directories=$(find "$folder_path" -maxdepth 1 -type d | wc -l )
num_directories=$((num_directories - 1))

echo "😂:$directories"
echo "$num_directories"
echo "🤣:$current_path"
echo "$0"
dirname "$0"

myARRAY=()
bSameName=false

#list directories in the form "./../Exercises/dirname/"
for dir in $folder_path/*/ 
do 
    dir=${dir%*/}  # remove the trailing "/"
    dir=${dir##*/} # print everything after the final "/"
    dir=${dir#??_} # remove the first two characters
    myARRAY+=("$dir")
    if [ "$dir" = $project_name ]
    then
        bSameName=true
    fi
done
echo "${myARRAY[@]}"
echo "$bSameName"
if [ "$bSameName" = false ]
then
    echo "exercise name is unique"
    new_num_dir=$((num_directories+1))
    if ((num_directories < 9)) 
    then
        prefix="0${new_num_dir}_"
    else
        prefix="${new_num_dir}_"
    fi    
else
    echo "exercise name existed. Cannot create exercise"
    exit 1
fi

function addExercise(){
    
    
    src_files="scripts.py"
    test_folder="test_${project_name}"
    testfd_files=("conftest.py" "pytest.ini")
    testprjctfiles="scripts_test.py"

    add_scripts=("def ${project_name}():" "    pass")
    add_test_scripts=("import pytest" "from src.scripts import ${project_name}" "pytest.mark.parametrize("input,expected",[()])" "def test_${project_name}(input, expected):" "    result=${project_name}(input)" "    assert result == expected")
    echo "$folder_path"
    echo "$project_name"
    echo "$prefix$project_name"
    

    # 1.) make the exercise folder:
    # mkdir "$folder_path/$prefix$project_name"
    echo "$folder_path/$prefix$project_name"
    
    # 2.) create folder src test and test/test_{project_name}
    exercise_folder="$folder_path/$prefix$project_name"
    folders=("src" "test" "test/test_${project_name}")
    common_files="__init__.py"
    for folder in "${folders[@]}"
    do
        # mkdir "$exercise_folder/$folder" # ie {src,test,test/test_projectname}
        echo "$exercise_folder/$folder"
        # touch "$exercise_folder/$folder/$common_files" #ie {__init__.py}
        echo "$exercise_folder/$folder/$common_files"
    done
    
    # 3.) Create scripts.py at src
    #touch src/scripts.py
    echo "$exercise_folder/"${folders[0]}""
    echo "$exercise_folder/"${folders[0]}"/$src_files"
    
    #4.) At test create test folder files
    echo "$exercise_folder/"${folders[1]}""
    test_fd="$exercise_folder/"${folders[1]}""

    for testfd in "${testfd_files[@]}"
    do
        # touch test/{conftest.py,pytest.ini}
        echo "$test_fd/$testfd"
    done
    
    # 5.) At test/test_{project_name} create test_scripts.py
    echo "$exercise_folder/"${folders[1]}"/$test_folder"
    testprjfd="$exercise_folder/"${folders[1]}"/$test_folder"

    # touch scripts.py
    echo "$testprjfd/$testprjctfiles"
    
    for script in "${add_scripts[@]}"
    do
        echo "$script" 
    done # > ${exercise_folder}/src/scripts.py

    for script in "${add_test_scripts[@]}"
    do
        echo "$script"
    done # > ${exercise_folder}/test/test_${project_name}/scripts_test.py
}

addExercise