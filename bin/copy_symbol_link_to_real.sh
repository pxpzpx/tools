#!/bin/sh

CURRENT_DIR=$(pwd)

# Read all file names into an array
FilesArray=($(find "./" -name "*.so.1"))

# Get length of an array
FilesIndex=${#FilesArray[@]}


# Use for loop read all directory names
for (( i=0; i<${FilesIndex}; i++ ));
do
    source="${FilesArray[$i]}"
    destination="$(echo "${source}" | sed 's/so.1/so/')"
    cp -vf "${source}" "${destination}"
done

exit 0;
