# -*- coding: iso-8859-1 -*-

# main.py
from src.analisis_estadistico import AnalisisEstadistico
from view.visualizacion import crear_histograma_normal, crear_histograma_superpuesto, mostrar_ocurrencias

if __name__ == "__main__":

    #Apartado 1 (src.analisis_estadistico.py)
    tamanio_muestra = 1000
    num_ensayos = 10
    probabilidad_de_exito = 0.5
    muestra_binomial = AnalisisEstadistico.generar_muestra_binomial(tamanio_muestra, num_ensayos, probabilidad_de_exito)
    #print(muestra_binomial) #comentar esta linea si va a ejecutar muestras grandes
    #mostrar_ocurrencias(muestra_binomial)
    
    #Apartado 2 (view.visualizacion.py)
    crear_histograma_normal(muestra_binomial, "histograma")

    #Apartado 3 
    lim_inferior_del_intervalo = 3
    lim_superior_del_intervalo = 7
    frec_relativa, prob_real, error = AnalisisEstadistico.estimar_probabilidad_intervalo(
        muestra_binomial, num_ensayos, probabilidad_de_exito, lim_inferior_del_intervalo, lim_superior_del_intervalo)
    print("Frecuencia relativa:", frec_relativa)
    print("Probabilidad real:", prob_real)
    print("Error:", error)

    #Apartado 4
    media = AnalisisEstadistico.calcular_media(muestra_binomial)
    varianza = AnalisisEstadistico.calcular_varianza(muestra_binomial)
    print("Media: ", media)
    print("Varianza: ", varianza)

    #Apartado 5
    muestra_nueva = AnalisisEstadistico.generar_muestra_nueva(muestra_binomial, media, varianza)
    #print([round(x, 3) for x in muestra_nueva]) #comentar esta linea si va a ejecutar muestras grandes
    media_muestra_nueva = AnalisisEstadistico.calcular_media(muestra_nueva)
    varianza_muestra_nueva = AnalisisEstadistico.calcular_varianza(muestra_nueva)
    print("Media_nueva: ", abs(round(media_muestra_nueva, 6)))
    print("Varianza_nueva: ", round(varianza_muestra_nueva, 6))

    #genero valores para la densidad normal
    x, densidad_normal = AnalisisEstadistico.generar_densidad_normal()
    crear_histograma_superpuesto(muestra_nueva, x, densidad_normal)









