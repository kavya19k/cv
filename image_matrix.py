from PIL import Image
import numpy as np
image =Image.open('img.png')
pixel_matrix = np.array(image)
print("Pixel Matrix:")
print(pixel_matrix)