from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
image =Image.open('img.png')
grayscale_image = image.convert("L")
pixel_matrix = np.array(grayscale_image)
histogram, bins = np.histogram(pixel_matrix, bins=256, range=(0, 256))
cdf = histogram.cumsum()
cdf_normalized = ((cdf - cdf.min()) * 255) / (cdf.max() - cdf.min())
equalization_lookup = np.interp(pixel_matrix, bins[:-1], cdf_normalized)
equalized_image = Image.fromarray(equalization_lookup.astype('uint8'))
equalized_histogram, _ = np.histogram(equalization_lookup, bins=256, range=(0, 256))
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.title("Equalized Image")
plt.imshow(equalized_image, cmap='gray')
plt.subplot(1, 2, 2)
plt.title("Equalized Histogram")
plt.xlabel("Pixel Value")
plt.ylabel("Frequency")
plt.bar(range(256), equalized_histogram)
plt.show()