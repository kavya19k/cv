import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
image = Image.open('img.png')
grayscale_image = np.array(image.convert("L"))
second_derivative_x = np.zeros_like(grayscale_image, dtype=np.int16)
for x in range(grayscale_image.shape[0]):
        for y in range(1, grayscale_image.shape[1] - 1):
            second_derivative_x[x, y] = grayscale_image[x, y - 1] + grayscale_image[x, y + 1] - 2 * grayscale_image[x, y]
print("Original Image Matrix:")
print(grayscale_image)
print("\nMatrix After 2nd Order Derivative (X):")
print(second_derivative_x)
plt.figure(figsize=(12, 4))

plt.subplot(1, 2, 1)
plt.title("Original Image Matrix")
plt.imshow(grayscale_image, cmap='gray', vmin=0, vmax=255)

plt.subplot(1, 2, 2)
plt.title("Matrix After 2nd Order Derivative (X)")
plt.imshow(second_derivative_x, cmap='gray', vmin=-255, vmax=255)

plt.show()