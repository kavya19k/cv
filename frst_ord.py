import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
image=Image.open('img.png')
grayscale_image = np.array(image.convert("L"))
derivative_x = np.zeros_like(grayscale_image, dtype=np.int16)
for x in range(grayscale_image.shape[0]):
        for y in range(grayscale_image.shape[1] - 1):
            derivative_x[x, y] = grayscale_image[x, y + 1] - grayscale_image[x, y]
print("Original Image Matrix:")
print(grayscale_image)
print("\nMatrix After 1st Order Derivative (X):")
print(derivative_x)
plt.figure(figsize=(12, 4))
plt.subplot(1, 2, 1)
plt.title("Original Image")
plt.imshow(grayscale_image, cmap='gray', vmin=0, vmax=255)

plt.subplot(1, 2, 2)
plt.title(" 1st Order Derivative (X)")
plt.imshow(derivative_x, cmap='gray', vmin=-255, vmax=255)

plt.show()