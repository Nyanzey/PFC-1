import torch
from torchvision import models, transforms
from torch.nn import functional as F
from PIL import Image
import numpy as np
from scipy.stats import entropy
import os
import argparse

# Load the pre-trained Inception v3 model
inception_model = models.inception_v3(pretrained=True, transform_input=False).eval()

# Image transformation pipeline
preprocess = transforms.Compose([
    transforms.Resize(299),
    transforms.CenterCrop(299),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

def get_predictions(images):
    # Transform the images and create a batch tensor
    if len(images) == 0:
        raise ValueError("No images provided for prediction")
    images = torch.stack([preprocess(image) for image in images])
    if torch.cuda.is_available():
        images = images.cuda()
        inception_model.cuda()
    with torch.no_grad():
        preds = inception_model(images)
    return F.softmax(preds, dim=1).cpu().numpy()

def inception_score(images, splits=10):
    # Get predictions for the images
    preds = get_predictions(images)
    if preds.size == 0:
        raise ValueError("No predictions obtained from the model")

    # Compute the IS score
    split_scores = []
    N = len(images)
    for k in range(splits):
        part = preds[k * (N // splits): (k + 1) * (N // splits), :]
        py = np.mean(part, axis=0)
        scores = [entropy(pyx, py) for pyx in part]
        split_scores.append(np.exp(np.mean(scores)))

    return np.mean(split_scores), np.std(split_scores)

def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        img_path = os.path.join(folder, filename)
        if img_path.endswith(('.png', '.jpg', '.jpeg')) and os.path.isfile(img_path):
            try:
                image = Image.open(img_path).convert('RGB')
                images.append(image)
            except Exception as e:
                print(f"Error loading image {img_path}: {e}")
    return images

if __name__ == "__main__":
    #parser = argparse.ArgumentParser(description="Calculate Inception Score for a folder of images")
    #parser.add_argument("folder", type=str, help="Path to the folder containing images")
    #args = parser.parse_args()

    # Load images from the specified folder
    images = load_images_from_folder("generation_original")

    if len(images) == 0:
        print("No images found in the specified folder.")
    else:
        # Calculate IS score
        try:
            mean_is, std_is = inception_score(images)
            print(f"Inception Score: {mean_is} ± {std_is}")
        except Exception as e:
            print(f"Error calculating Inception Score: {e}")