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
# project_name="$1"
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
    if [ "$dir" = $1 ]
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
echo "$prefix$1"