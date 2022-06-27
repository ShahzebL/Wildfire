import numpy as np
import PIL
from PIL import Image
import matplotlib.pyplot as plt
import cfo
forest = cfo.api()


# res = forest.search(geography="MendocinoCounty", metric="CanopyCover")

# print(res)
# print(type(res))
import cv2
PIL.Image.MAX_IMAGE_PIXELS = 9331200000

def heatmap2d(arr: np.ndarray):
    plt.imshow(arr, cmap='viridis', vmin=130, vmax=200)
    plt.colorbar()
    plt.title("Santa Clara County Surface Fuels (Spread Rate)")
#     plt.savefig('NevadaMaps/NevadaCounty-SurfaceFuels2.png')
    plt.show()



# test_array = np.arange(100 * 100).reshape(100, 100)


# 
# im = Image.open('Nevada/NevadaCounty-Vegetation-SurfaceFuels-2020-Summer-00010m.tif')
im = Image.open("Santa-Clara/SantaClara-Vegetation-SurfaceFuels-2020-Summer-00010m.tif")
#SantaClara-Wildfire-Hazard-2020-Summer-00010m
imarray = np.array(im)
# imarray = imarray[5000:7000, 6500:8000]
print(imarray.shape)
heatmap2d(imarray)
# ax = sns.heatmap(imarray, linewidth=0.5)
# plt.show()

# plt.imshow(imarray, cmap='hot', interpolation='nearest')
# plt.show()

# heatmap = cv2.applyColorMap(imarray, cv2.COLORMAP_HOT)
# cv2.imshow('heatmap', heatmap)
# cv2.waitKey()
# print(np.amax(imarray))

