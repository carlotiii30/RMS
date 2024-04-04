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


# - - - - Análisis de los retardos entre paquetes - - - -

# Calculamos los retardos entre paquetes como se ha mencionado
df["retardo"] = df["Time"] - df["Time"].shift(1)


# - - - - Histograma de los retardos entre paquetes - - - -

# Calculamos los bins
bins = np.arange(0, 0.0001, 0.000001)

# Establecemos el estilo de la gráfica
plt.style.use("ggplot")

# Creamos una figura más grande
plt.figure(figsize=(10, 6))

# Graficamos el histograma
plt.hist(df["retardo"], bins=bins, color="skyblue", edgecolor="black")

# Añadimos títulos y etiquetas
plt.title("Histograma de retardos entre paquetes", fontsize=16)
plt.xlabel("Retardo (s)", fontsize=14)
plt.ylabel("Frecuencia", fontsize=14)

# Aumentamos el tamaño de las etiquetas de los ejes
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

# Añadimos una cuadrícula para mejorar la legibilidad
plt.grid(True)

# Guardamos la gráfica como un archivo PNG
plt.savefig(os.path.join(dir_path, "graficas/retardos.png"))

# Mostramos la gráfica
plt.show()
