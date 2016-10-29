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
