from PIL import Image

def divide_image_vertically(image_path, num_slices):
    # Open the image
    image = Image.open(image_path)
    image_width, image_height = image.size
    
    # Calculate the width of each slice
    slice_width = image_width // num_slices
    
    # Create and save each slice
    for i in range(num_slices):
        left = i * slice_width
        right = (i + 1) * slice_width
        if i == num_slices - 1: 
            right = image_width
        
        box = (left, 0, right, image_height)
        slice_image = image.crop(box)
        slice_image.save(f'slice_{i + 1}.png')
        print(f'Saved slice_{i + 1}.png')