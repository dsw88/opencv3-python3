from operations import *

img = load_image('test-image.jpg', cv2.IMREAD_COLOR)

# Redact the image
# draw_rectangle(img, (0,0), (400,400), (0,0,0))

# Get some metadata about image and pixel
# px = img[100,100]
# print(px)
print(img.shape)


# RESIZE THE IMAGE
# ratio = 100.0 / img.shape[1]
# dim = (100, int(img.shape[0] * ratio)) # Preserve aspect ratio
# resized = resize(img, dim)

# ROTATE THE IMAGE
# rotated = rotate(img, 60)

cropped = img[400:800, 800:1200]


# my_roi = img[0:100, 0:100]
img[0:100, 0:100, 0] = 2
# print(img.dtype)

# Remove blue from color space
# img[:,:,0] = 2

save_image(cropped, 'converted-image2.tif')