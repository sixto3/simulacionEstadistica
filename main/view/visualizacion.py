# visualizacion.py

import matplotlib.pyplot as plt
import numpy as np
import collections


def crear_histograma_normal(muestra_binomial, nombre_archivo):

    fig, ax = plt.subplots()
    bin_edges = np.arange(min(muestra_binomial) - 0.5, max(muestra_binomial) + 1.5, 1)
    
    # Generar histograma con los límites de los bins ajustados
    ax.hist(muestra_binomial, bins=bin_edges, align='mid', edgecolor='black')
    ax.set_xlabel('Numero de exitos')
    ax.set_ylabel('Frecuencia')
    ax.set_title('Distribucion de frecuencias')
    #plt.xticks(np.arange(min(muestra_binomial), max(muestra_binomial)+1, 1))
    ax.set_xticks(range(0, 11))
    ax.set_gid(True)
    
    # Crear histograma
    fig.savefig(nombre_archivo + ".png")

   

def crear_histograma_superpuesto(muestra, x, densidad_normal):
    fig, ax = plt.subplots()
    bin_edges = np.arange(min(muestra) - 0.5, max(muestra) + 1.5, 1)
    
    # Generar histograma con los límites de los bins ajustados
    n, bins, patches = ax.hist(muestra, bins=bin_edges, edgecolor='black', align='mid')
    escala = np.sum (n * np.diff(bins))
    densidad_normal *= escala
    ax.plot(x, densidad_normal, color='red', label='Distribucion normal')
    ax.set_xlabel('Valores')
    ax.set_ylabel('Frecuencia')
    ax.set_xticks(range(-5, 5))
    ax.set_gid(True)
    ax.legend()

    fig.savefig("Histograma_nuevo.png")


def mostrar_ocurrencias(muestra):
    conteo = collections.Counter(muestra)
    for elemento, frecuencia in sorted(conteo.items()):
        print(f"{elemento} --> {frecuencia}")
