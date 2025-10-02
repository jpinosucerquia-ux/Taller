import numpy as np
import matplotlib.pyplot as plt

# Estilo de gráficos
plt.style.use('ggplot')

# Generar 1000 datos aleatorios (media=20, desviación=2)
data = np.random.randn(1000) * 2 + 20   

# Histograma normalizado con separación entre barras
plt.hist(data, bins=50, density=True, alpha=0.5, 
         histtype='stepfilled', color='steelblue', edgecolor='None',)   # <-- controla separación entre barras

# Calcular media y desviación
mu, sigma = np.mean(data), np.std(data)

# Valores para la curva normal
x = np.linspace(12, 30, 200)
pdf = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-((x - mu)**2) / (2 * sigma**2))

# Dibujar la curva
plt.plot(x, pdf, 'm--', linewidth=2, label="Curva normal")

# Etiquetas y título
plt.title("Histograma")
plt.xlabel("Valor x")
plt.ylabel("Probabilidad")
plt.legend()

# Ajustar límites de ejes
plt.xlim(12, 30)
plt.ylim(0.00, 0.25)

plt.show()



# Valores de x
x = np.linspace(-10, 10, 400)

# Definición de funciones
y1 = 2*x + 1
y2 = -x**2

# Gráfico
plt.plot(x, y1, label="y = 2x + 1", color="blue")
plt.plot(x, y2, label="y = -x²", color="red")

# Ejes y estilo
plt.axhline(0, color="black", linewidth=0.5)
plt.axvline(0, color="black", linewidth=0.5)
plt.grid(True, linestyle="--", alpha=0.6)

plt.title("Funciones en el mismo plano")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()