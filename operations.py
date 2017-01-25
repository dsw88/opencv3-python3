import numpy as np
import cv2

def load_image(image_src, image_value):
    return cv2.imread(image_src, image_value)

def save_image(img, image_dest):
    cv2.imwrite(image_dest, img)

def draw_rectangle(img, top_left, bottom_right, color):
    img = cv2.rectangle(img, top_left, bottom_right, color, -1)

def convert_to_grayscale(image_src, image_dest):
    img = load_image(image_src, cv2.IMREAD_GRAYSCALE)
    save_image(img, image_dest)

def resize(img, dimension):
    return cv2.resize(img, dimension, interpolation = cv2.INTER_AREA)

def rotate(img, degrees):
    (h, w) = img.shape[:2]
    center = (w/2, h/2)
    M = cv2.getRotationMatrix2D(center, degrees, 1.0)
    return cv2.warpAffine(img, M, (w,h))
    