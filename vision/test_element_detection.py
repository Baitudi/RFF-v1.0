import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image_path = 'element.png'
image = cv2.imread(image_path)

if image is None:
    print("Error: Image not found.")
    exit()

# Convert BGR to RGB for matplotlib display
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Split channels
b_channel, g_channel, r_channel = cv2.split(image)

# Plot the histograms
plt.figure(figsize=(16, 6))

plt.subplot(1, 4, 1)
plt.imshow(image_rgb)
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 4, 2)
plt.hist(b_channel.ravel(), bins=256, color='blue', alpha=0.7)
plt.title('Blue Channel')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')

plt.subplot(1, 4, 3)
plt.hist(g_channel.ravel(), bins=256, color='green', alpha=0.7)
plt.title('Green Channel')
plt.xlabel('Pixel Value')

plt.subplot(1, 4, 4)
plt.hist(r_channel.ravel(), bins=256, color='red', alpha=0.7)
plt.title('Red Channel')
plt.xlabel('Pixel Value')

plt.tight_layout()
plt.show()
