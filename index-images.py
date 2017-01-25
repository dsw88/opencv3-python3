import mahotas
import numpy as np
import glob
import pickle
import cv2

class ZernikeMoments:
    def __init__(self, radius):
        self.radius = radius
    
    def describe(self, image):
        return mahotas.features.zernike_moments(image, self.radius)

desc = ZernikeMoments(21) # Radius was chosen by tutorial author.
index = {}

for spritePath in glob.glob('./sprites/*.png'):
    pokemon = spritePath[spritePath.rfind("/") + 1:].replace(".png", "")
    image = cv2.imread(spritePath)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Pad image with extra white pixels to ensure the edges of the pokemon are not up against the borders of the image
    image = cv2.copyMakeBorder(image, 15, 15, 15, 15, cv2.BORDER_CONSTANT, value=255)

    # Invert the image and threshold it 
    thresh = cv2.bitwise_not(image)
    thresh[thresh > 0] = 255

    outline = np.zeros(image.shape, dtype = 'uint8')
    (_, cnts, _) = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[0]
    cv2.drawContours(outline, [cnts], -1, 255, -1)

    moments = desc.describe(outline)
    index[pokemon] = moments

f = open("pkmn_index", 'wb')
f.write(pickle.dumps(index))
f.close()