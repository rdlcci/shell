#!/usr/bin/env bash
# creates a project structure with the name provided in the 1st argument
# also adds name to readme.md based on 2nd argument
# process :  
# copy this file where the project needs to be created
# run the following in terminal, by replacing the arguments in caps
# 1. chmod +x creator.sh
# 2. ./creator.sh PROJECTNAME YOURNAME

mkdir $1
cd $1
mkdir code data output model embedding test notebook presentations 
echo "## ${1} by ${2}" >> README.md

# delete them all, dont uncomment this 
##### rm -r code data output model embedding test notebook README.md
##### rm -rf $1


#### Feel free to modify and recommend changes for the team