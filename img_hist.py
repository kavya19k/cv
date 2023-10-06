import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
image=Image.open('img.png')
grayscale_image = image.convert("L")
pixel_matrix = np.array(grayscale_image)
histogram = np.histogram(pixel_matrix, bins=np.arange(256))
plt.figure(figsize=(8, 6))
plt.title("Pixel Value Frequency Histogram")
plt.xlabel("Pixel Value")
plt.ylabel("Frequency")
plt.bar(histogram[1][:-1], histogram[0], width=1, align='center')
plt.show()