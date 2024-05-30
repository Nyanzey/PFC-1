import os
import shutil
import random
import argparse
from PIL import Image

def resize_images(input_dir, output_dir, size):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    resized_image_paths = []
    for filename in os.listdir(input_dir):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            img_path = os.path.join(input_dir, filename)
            img = Image.open(img_path)
            img_resized = img.resize(size, Image.LANCZOS)
            output_path = os.path.join(output_dir, filename)
            img_resized.save(output_path)
            resized_image_paths.append(output_path)

    return resized_image_paths

def balance_datasets(generated_paths, evaluation_paths, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    balanced_paths = list(generated_paths)

    if len(generated_paths) < len(evaluation_paths):
        num_additional_images = len(evaluation_paths) - len(generated_paths)
        additional_images = random.sample(evaluation_paths, num_additional_images)
        balanced_paths.extend(additional_images)

    for img_path in balanced_paths:
        shutil.copy(img_path, output_dir)

    return balanced_paths

def main():
    parser = argparse.ArgumentParser(description='Resize images and balance datasets.')
    parser.add_argument('--galip_generated_input_dir', type=str, required=True, help='Path to the generated input directory.')
    parser.add_argument('--galip_generated_output_dir', type=str, required=True, help='Path to the generated output directory.')
    parser.add_argument('--gligen_generated_input_dir', type=str, required=True, help='Path to the generated input directory.')
    parser.add_argument('--gligen_generated_output_dir', type=str, required=True, help='Path to the generated output directory.')

    parser.add_argument('--evaluation_input_dir', type=str, required=True, help='Path to the evaluation input directory.')
    parser.add_argument('--evaluation_output_dir', type=str, required=True, help='Path to the evaluation output directory.')
    parser.add_argument('--balanced_output_dir', type=str, required=True, help='Path to the balanced output directory.')

    parser.add_argument('--resize_width', type=int, required=True, help='Width to resize images to.')
    parser.add_argument('--resize_height', type=int, required=True, help='Height to resize images to.')

    args = parser.parse_args()

    resize_size = (args.resize_width, args.resize_height)

    galip_generated_resized_paths = resize_images(args.galip_generated_input_dir, args.galip_generated_output_dir, resize_size)
    gligen_generated_resized_paths = resize_images(args.gligen_generated_input_dir, args.gligen_generated_output_dir, resize_size)
    evaluation_resized_paths = resize_images(args.evaluation_input_dir, args.evaluation_output_dir, resize_size)

    if len(galip_generated_resized_paths) < len(gligen_generated_resized_paths):
        balanced_dataset_paths = balance_datasets(galip_generated_resized_paths, evaluation_resized_paths, args.balanced_output_dir)
    else:
        balanced_dataset_paths = balance_datasets(gligen_generated_resized_paths, evaluation_resized_paths, args.balanced_output_dir)
    
    print(len(balanced_dataset_paths))


if __name__ == "__main__":
    main()