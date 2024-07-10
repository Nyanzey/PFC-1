#!/bin/bash

# Define sets of values for prompt, phrases, and locations
prompts=(
    "A sunset over a mountain range"
)
phrases=("")
locations=("")

# Loop through the indices of the sets
for i in "${!prompts[@]}"
do
    python3 gligen_inference.py --prompt "${prompts[i]}" --phrase "${phrases[0]}" --location "${locations[0]}"
done