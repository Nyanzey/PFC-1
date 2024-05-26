#!/bin/bash

# Paths to the directories
DIR1="./ProcessedEval"
DIR2="./ProcessedGalip"
DIR3="./ProcessedGligen"
DIR4="./BalancedEval"

# Function to clear files in a directory
clear_directory() {
    local dir=$1
    if [ -d "$dir" ]; then
        echo "Clearing files in $dir"
        rm -rf "$dir"/*
    else
        echo "Directory $dir does not exist"
    fi
}

# Clear the directories
clear_directory $DIR1
clear_directory $DIR2
clear_directory $DIR3
clear_directory $DIR4

echo "All specified directories have been cleared."