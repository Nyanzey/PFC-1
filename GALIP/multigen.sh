#!/bin/bash

# List of arguments to pass to the Python script
prompts=(
    "A sunset over a mountain range"
)


# Loop through the list of arguments
for prompt in "${prompts[@]}"
do
    python3 generate.py "$prompt"
done
