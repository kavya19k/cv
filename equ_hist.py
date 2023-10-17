import cv2
import matplotlib.pyplot as plt

def histogram(pixel_matrix, bins=256, range=(0, 256)):
    histogram = [0] * bins
    min_range, max_range = range

    for row in pixel_matrix:
        for pixel_value in row:
            if min_range <= pixel_value < max_range:
                bin_index = int((pixel_value - min_range) / (max_range - min_range) * bins)
                histogram[bin_index] += 1

    return histogram, list(range(min_range, max_range, int((max_range - min_range) / bins)))

def main():
    # Load an image
    image = cv2.imread("img.png", cv2.IMREAD_GRAYSCALE)

    # Calculate the histogram
    hist, bin_edges = histogram(image, bins=256, range=(0, 256))

    # Display the original image
    plt.subplot(121)
    plt.imshow(image, cmap='gray')
    plt.title('Original Image')

    # Display the
