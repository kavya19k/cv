import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from PIL import Image
def gaussian_filter(image, sigma=1):
    # Create a 5x5 Gaussian kernel
    size = int(6 * sigma + 1)
    if size % 2 == 0:
        size += 1
    kernel = np.fromfunction(
        lambda x, y: (1/ (2 * np.pi * sigma ** 2)) * 
                      np.exp(-((x - (size // 2)) ** 2 + (y - (size // 2)) ** 2) / (2 * sigma ** 2)),
        (size, size)
    )
    kernel = kernel / np.sum(kernel)
    smoothed_image = signal.convolve2d(image, kernel, mode='same', boundary='wrap')

    return smoothed_image

img=Image.open('img.png')
grayscale_image = np.array(img.convert("L"))
smoothed_image = gaussian_filter(grayscale_image, sigma=1)
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.title("Original Image")
plt.imshow(grayscale_image, cmap='gray')

plt.subplot(1, 2, 2)
plt.title("Smoothed Image")
plt.imshow(smoothed_image, cmap='gray')

plt.show()