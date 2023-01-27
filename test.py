image_path = "/home/bull/Pictures/Wallpapers/astro.jpg"

import matplotlib.image as img
import pandas as pd
from scipy.cluster.vq import whiten

my_img = img.imread(image_path)

r = []
g = []
b = []

print("appending values...")
for row in my_img:
    for temp_r, temp_g, temp_b in row:
        r.append(temp_r)
        g.append(temp_g)
        b.append(temp_b)

img_df = pd.DataFrame({"red": r, "green": g, "blue": b})

# scale the values
print("scaling")
img_df["scaled_color_red"] = whiten(img_df["red"])
img_df["scaled_color_blue"] = whiten(img_df["blue"])
img_df["scaled_color_green"] = whiten(img_df["green"])

print(img_df.head)
