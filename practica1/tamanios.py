# Importamos las librerías necesarias
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

# - - - - Carga de datos - - - -

# Obtención de la ruta del directorio actual
dir_path = os.path.dirname(os.path.realpath(__file__))

# Obtención de la ruta del archivo de datos, que se encuentra en el mismo
file_path = os.path.join(dir_path, "datos.csv")

# Carga del archivo de datos
df = pd.read_csv(file_path)


# - - - - Histograma de los tamaños de los paquetes - - - -

# Calculamos el número de bins usando la regla de la raíz cuadrada
bins = int(np.sqrt(len(df["Length"])))

# Establecemos el estilo de la gráfica
plt.style.use("ggplot")

# Creamos una figura más grande
plt.figure(figsize=(10, 6))

# Graficamos el histograma
plt.hist(df["Length"], bins=bins, edgecolor="black", color="turquoise")

# Añadimos títulos y etiquetas
plt.title("Histograma de Tamaños de Paquetes", fontsize=16)
plt.xlabel("Tamaño del Paquete", fontsize=14)
plt.ylabel("Frecuencia", fontsize=14)

# Aumentamos el tamaño de las etiquetas de los ejes
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

# Añadimos una cuadrícula para mejorar la legibilidad
plt.grid(True)

# Guardamos la gráfica como un archivo PNG
plt.savefig(os.path.join(dir_path, "graficas/tamanios.png"))

# Mostramos la gráfica
plt.show()
