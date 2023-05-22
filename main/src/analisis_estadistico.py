# analisis_estadistico.py

import random
import numpy as np
from scipy import stats


class AnalisisEstadistico:
    @staticmethod
    def generar_muestra_binomial(tam, n, p):
        muestra = []
        for _ in range(tam):
            exitos = 0
            for _ in range(n):
                resultado_ensayo = random.uniform(0, 1) 
                if resultado_ensayo < p:  # probabilidad de éxito
                    exitos += 1
            muestra.append(exitos)
        return muestra

    def estimar_probabilidad_intervalo(muestra, n, p, a, b):
        muestra = np.array(muestra)
        frec_relativa = np.mean((muestra >= a) & (muestra <= b))
        prob_real = stats.binom.cdf(b, n, p) - stats.binom.cdf(a-1, n, p)
        error = abs(frec_relativa - prob_real)

        return frec_relativa, prob_real, error

    def calcular_media(muestra):
        return np.mean(muestra)

    def calcular_varianza(muestra):
        return np.var(muestra)
        
    def generar_muestra_nueva(muestra_binomial, media, varianza):
        raiz_varianza = np.sqrt(varianza)
        muestra_nueva = [((x-media)/(raiz_varianza)) for x in muestra_binomial]
        return muestra_nueva

    def generar_densidad_normal():
        x = np.linspace(-4, 4, 500)
        densidad_normal = (1 / np.sqrt(2 * np.pi)) * np.exp(-0.5 * x**2)
        return x, densidad_normal

    