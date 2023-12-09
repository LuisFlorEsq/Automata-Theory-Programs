import matplotlib.pyplot as plt

# Inicializa las listas para cada lote de datos
x_batch = []
y_batch = []
batch_size = 10000000
plot_counter = 0

import matplotlib.pyplot as plt

# Inicializa las listas para cada lote de datos
x_batch = []
y_batch = []
batch_size = 6000000

with open("cantidad_unos.txt", "r") as archivo:
    for linea in archivo:
        datos = linea.strip().split('\t')
        x_batch.append(int(datos[0]))
        y_batch.append(int(datos[1]))

        # Cuando alcanzas el tamaño del lote, grafica los datos y luego reinicia las listas
        if len(x_batch) == batch_size:
            plt.plot(x_batch, y_batch)
            x_batch = []
            y_batch = []

    # Grafica los datos restantes si no forman un lote completo
    if x_batch:
        plt.plot(x_batch, y_batch)

plt.xlabel('Número de Cadena')
plt.ylabel('Número de Unos de la Cadena')
plt.title('Gráfico de tus datos')
plt.show()
