import time

import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from sklearn.cluster import KMeans

UPLOAD_FOLDER = "./static/uploads"


def show_img_compare(img_1, img_2):
    f, ax = plt.subplots(1, 2, figsize=(10, 10))
    ax[0].imshow(img_1)
    ax[1].imshow(img_2)
    ax[0].axis("off")
    ax[1].axis("off")
    f.tight_layout()
    plt.show()


def get_average():
    # GET AVERAGE
    temp = img_1.copy()
    temp[:, :, 0], temp[:, :, 1], temp[:, :, 2] = np.average(img_1, axis=(0, 1))

    temp_2 = img_2.copy()
    temp_2[:, :, 0], temp_2[:, :, 1], temp_2[:, :, 2] = np.average(img_2, axis=(0, 1))

    show_img_compare(temp, img_1)
    show_img_compare(temp_2, img_2)


def get_most_common():
    # reshape destructures the array so that it is just a list of lists
    img_temp = img_1.copy()

    # np.unique returns the SORTED unique elements of an array, can pass in
    # a parameter return_counts which counts the number of times each unique value
    # comes up in the input array
    # the axis parameter makes it so it doesn't get flattened
    unique, counts = np.unique(img_temp.reshape(-1, 3), return_counts=True, axis=0)
    img_temp[:, :, 0], img_temp[:, :, 1], img_temp[:, :, 2] = unique[np.argmax(counts)]

    show_img_compare(img_1, img_temp)


def palette(clusters):
    width = 300
    palette = np.zeros((50, width, 3), np.uint8)
    steps = width / clusters.cluster_centers_.shape[0]
    for idx, centers in enumerate(clusters.cluster_centers_):
        palette[:, int(idx * steps) : (int((idx + 1) * steps)), :] = centers
    return palette


def get_colors(PIL_image):
    dim = (9, 6)
    print("reading image")
    img = np.array(PIL_image)
    img = cv.resize(img, dim, interpolation=cv.INTER_AREA)

    print("reversing array")
    # img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

    print("clustering")
    clt = KMeans(n_clusters=5, n_init=10)

    print("fitting")
    clt.fit(img.reshape(-1, 3))

    print("showing image")

    # index 0 = the image array of common colours
    # index 1 = the array of arrays of common colours
    return (palette(clt), clt.cluster_centers_)


def convert_RGB_to_hex(R, G, B):
    # RGB is a list of RGB [R, G, B]
    R = int(R)
    G = int(G)
    B = int(B)

    return "#{:X}{:X}{:X}".format(R, G, B)


def get_all_hexes(common_color_RGBs):

    hexes = []
    for color in common_color_RGBs:
        R, G, B = color
        hexes.append((convert_RGB_to_hex(R, G, B)))

    return hexes


def get_image_pallette(img_file):
    img = Image.open(img_file)
    color_pallette, color_RGBs = get_colors(img)
    color_hexes = get_all_hexes(color_RGBs)

    return color_hexes
