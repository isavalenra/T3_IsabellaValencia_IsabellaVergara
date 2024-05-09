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

    def transformacion(self):
        ima = self.__img
        plt.subplot(3, 2, 1)
        plt.title('Imagen sin transformación')
        plt.axis('off')
        plt.imshow(ima)
        imap =cv2.cvtColor(ima,cv2.COLOR_BGR2RGB)
        _,imapB = cv2.threshold(imap[:,:,2], 127, 255, cv2.THRESH_BINARY)
        plt.subplot(3, 2, 2)
        plt.title('Imagen binaria')
        plt.axis('off')
        plt.imshow(imapB, cmap='gray', vmin=0, vmax=255)
        
        #Apertura, dilatación y erosión:
        kernel = np.ones((5, 5), np.uint8)
        imapB = cv2.morphologyEx(imapB, cv2.MORPH_OPEN, kernel) 
        ima2 = cv2.dilate(imapB,kernel,iterations = 2)
        ima2 = cv2.erode(ima2,kernel,iterations = 2)
        num_cells, labeled_image = cv2.connectedComponents(ima2)

        # Imprimir el número de células
        print("Número de células encontradas:", num_cells - 1)  # Restamos 1 para excluir el fondo

        # Graficar el resultado
        plt.subplot(3, 2, 3)
        plt.imshow(labeled_image, cmap='jet')  # Usamos 'jet' colormap para visualizar las etiquetas
        plt.title('Imagen con células etiquetadas')
        plt.axis('off')
        plt.show()
        
def main():
    while True:
        print("\nMenú:")
        print("a. Ingresar img")
        print("b. Ingresar DYCOM")
        print("c. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == 'a':
            imagen = Imagenes()

            ruta = input("Ingrese la ruta del archivo: ")
            imagen.cargar_img(ruta)
            imagen.transformacion()

        elif opcion == 'b':
          pass

        elif opcion == 'c':
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == '__main__':
    main()