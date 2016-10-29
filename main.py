from operations import *

img = load_image('test-image.jpg', cv2.IMREAD_COLOR)

# Redact the image
# draw_rectangle(img, (0,0), (400,400), (0,0,0))

# Get some metadata about image and pixel
# px = img[100,100]
# print(px)
# print(img.shape)
# print(img.dtype)

# Remove blue from color space
# img[:,:,0] = 2

save_image(img, 'converted-image.jpg')