import cv2
import numpy as np

from mcdwt.quantizator import quantizator, unQuantizator

coef = 2

frame = cv2.imread("../test_images/001.png")
outputQuantizated = quantizator(frame, coef)

cv2.imwrite("../test_images/001quantizates.png", outputQuantizated)

outputUnQuantizated = unQuantizator(outputQuantizated, coef)
cv2.imwrite("../test_images/001unQuantizates.png", outputUnQuantizated)