import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from sklearn.cluster import KMeans

# image = Image.open("./static/uploads/bluelilies.jpg")


# pixel_array = np.array(image)

# colours = {}

# R, G, B = pixel_array[100, 150]

# rgb_string = f"{R}, {G}, {B}"

# print(np.average(pixel_array, axis=(0, 1)))

# img = Image.fromarray(pixel_array, "RGB")
# img.show()


def show_img_compare(img_1, img_2):
    f, ax = plt.subplots(1, 2, figsize=(10, 10))
    ax[0].imshow(img_1)
    ax[1].imshow(img_2)
    ax[0].axis("off")
    ax[1].axis("off")
    f.tight_layout()
    plt.show()


# Get image arrays
img_1 = cv.imread("./static/uploads/bluelilies.jpg")
img_1 = cv.cvtColor(img_1, cv.COLOR_BGR2RGB)
img_2 = cv.imread("./static/uploads/1994716.jpg")
img_2 = cv.cvtColor(img_2, cv.COLOR_BGR2RGB)

# resize image
dimensions = (500, 300)

img_1 = cv.resize(img_1, dimensions, interpolation=cv.INTER_AREA)
img_2 = cv.resize(img_2, dimensions, interpolation=cv.INTER_AREA)


def get_average():
    # GET AVERAGE
    temp = img_1.copy()
    temp[:, :, 0], temp[:, :, 1], temp[:, :, 2] = np.average(img_1, axis=(0, 1))

    temp_2 = img_2.copy()
    temp_2[:, :, 0], temp_2[:, :, 1], temp_2[:, :, 2] = np.average(img_2, axis=(0, 1))

    show_img_compare(temp, img_1)
    show_img_compare(temp_2, img_2)


def palette(clusters):
    width = 300
    palette = np.zeros((50, width, 3), np.uint8)
    steps = width / clusters.cluster_centers_.shape[0]
    for idx, centers in enumerate(clusters.cluster_centers_):
        palette[:, int(idx * steps) : (int((idx + 1) * steps)), :] = centers
    return palette


clt = KMeans(n_clusters=5)
clt.fit(img_1.reshape(-1, 3))

show_img_compare(img_1, palette(clt))
