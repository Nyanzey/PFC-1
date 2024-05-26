#!/bin/bash

# Paths to the directories
GALIP_GENERATED_INPUT_DIR="./GalipData"
GLIGEN_GENERATED_INPUT_DIR="./GligenData"
EVALUATION_INPUT_DIR="./EvalData"

GALIP_GENERATED_OUTPUT_DIR="./ProcessedGalip"
GLIGEN_GENERATED_OUTPUT_DIR="./ProcessedGligen"
EVALUATION_OUTPUT_DIR="./ProcessedEval"

BALANCED_OUTPUT_DIR="./BalancedEval"

# Desired resize size
RESIZE_WIDTH=512
RESIZE_HEIGHT=512

# Run the Python script with the specified arguments
python3 process_data.py \
    --galip_generated_input_dir $GALIP_GENERATED_INPUT_DIR \
    --galip_generated_output_dir $GALIP_GENERATED_OUTPUT_DIR \
    --gligen_generated_input_dir $GLIGEN_GENERATED_INPUT_DIR \
    --gligen_generated_output_dir $GLIGEN_GENERATED_OUTPUT_DIR \
    --evaluation_input_dir $EVALUATION_INPUT_DIR \
    --evaluation_output_dir $EVALUATION_OUTPUT_DIR \
    --balanced_output_dir $BALANCED_OUTPUT_DIR \
    --resize_width $RESIZE_WIDTH \
    --resize_height $RESIZE_HEIGHT

# Run FID calculation using pytorch-fid
echo "------------- FID score (GALIP) -------------"
python3 -m pytorch_fid $GALIP_GENERATED_OUTPUT_DIR $BALANCED_OUTPUT_DIR --device cuda
echo "------------- FID score (GLIGEN) -------------"
python3 -m pytorch_fid $GLIGEN_GENERATED_OUTPUT_DIR $BALANCED_OUTPUT_DIR --device cuda