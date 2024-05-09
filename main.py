import cv2
import numpy as np
import matplotlib.pyplot as plt
import pydicom 
import os

class Imagenes:
    def __init__(self):
        self.__img = []

    def cargar_img(self,ruta):
        self.__img = cv2.imread(ruta)

    