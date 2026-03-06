##
## EPITECH PROJECT, 2026
## cvrie
## File description:
## extract_dataset
##

import numpy as np
import os
from PIL import Image

images = np.load("dataset/train_images.npy")
labels = np.load("dataset/train_labels.npy").flatten()

print("labels shape: ", labels.shape)

#i need to create the categories based of yhe labels, which i don't yet know
categories = ["normal", "pneumonia"]

base_dir = "dataset/Training"

for c in categories:
    os.makedirs(os.path.join(base_dir, c), exist_ok=True)

for i, (img, label) in enumerate(zip(images, labels)):

    category = categories[label]

    path = os.path.join(base_dir, category, f"{i}.png")

    img = (img * 255).astype("uint8")

    Image.fromarray(img).save(path)

print("Done.")