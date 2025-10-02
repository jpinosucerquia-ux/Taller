import numpy as np
import matplotlib.pyplot as plt

# 1. Crear un vector de size = 720, con valores aleatorios
vector = np.random.randn(720)

# 2. Hacer reshape de (120, 6)
matriz = vector.reshape(120, 6)

# 3. Transpuesta de la matriz y dos copias con distinto orden
matriz_T_F = np.transpose(matriz).copy(order="F")
matriz_T_C = np.transpose(matriz).copy(order="C")

# Verificación (opcional)
print("Forma matriz original:", matriz.shape)
print("Forma transpuesta F:", matriz_T_F.shape)
print("Forma transpuesta C:", matriz_T_C.shape)

# 4. Subplot con 6 paneles, usando versión “a mano” con proporciones distintas
fig, axs = plt.subplots(2, 3, figsize=(12, 6))

# Seleccionar 6 filas de la matriz transpuesta para graficar
data_rows = matriz_T_C[:6, :]

# 5. Diferentes tipos de gráficos
# Panel 1 - Línea
axs[0, 0].plot(data_rows[0], color="blue", label="Plot")
axs[0, 0].set_title("Gráfico de líneas")
axs[0, 0].legend()
axs[0, 0].grid(True)

# Panel 2 - Dispersión
axs[0, 1].scatter(range(len(data_rows[1])), data_rows[1], color="red", label="Scatter")
axs[0, 1].set_title("Dispersión")
axs[0, 1].legend()
axs[0, 1].grid(True)

# Panel 3 - Barras
axs[0, 2].bar(range(len(data_rows[2])), data_rows[2], color="green", label="Bar")
axs[0, 2].set_title("Barras")
axs[0, 2].legend()
axs[0, 2].grid(True)

# Panel 4 - Histograma
axs[1, 0].hist(data_rows[3], bins=10, color="purple", alpha=0.7, label="Histograma")
axs[1, 0].set_title("Histograma")
axs[1, 0].legend()
axs[1, 0].grid(True)

# Panel 5 - Pie chart
axs[1, 1].pie(np.abs(data_rows[4][:6]), labels=[f"c{i}" for i in range(6)], autopct="%1.1f%%")
axs[1, 1].set_title("Gráfico circular")

# Panel 6 - Línea con estilo
axs[1, 2].plot(data_rows[5], "m--", linewidth=2, label="Estilo especial")
axs[1, 2].set_title("Línea discontinua")
axs[1, 2].legend()
axs[1, 2].grid(True)

# Ajustar espacios
plt.tight_layout()
plt.show()