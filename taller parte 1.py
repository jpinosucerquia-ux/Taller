import numpy as np
import matplotlib.pyplot as plt

# Crear datos de 0 a 360 grados
x = np.arange(0, 361)           # ángulos en grados
x_rad = np.radians(x)           # conversión a radianes
y = np.sin(x_rad)               # calcular seno


# Datos

x = np.arange(0, 361)      # ángulos en grados
x_rad = np.radians(x)      # conversión a radianes
y_sin = np.sin(x_rad)      # seno
y_cos = np.cos(x_rad)      # coseno


# Figura 1: solo función seno

plt.figure()
plt.plot(x_rad, y_sin, 'm--', label="Función seno")
plt.xlabel('Ángulo (rad)')
plt.ylabel('sin(x)')
plt.title('Función seno')
plt.legend()
plt.grid(True)
plt.show()


# Figura 2: seno y coseno

plt.figure()
plt.plot(x_rad, y_sin, 'm--', label="Función seno")
plt.plot(x_rad, y_cos, 'g-', label="Función coseno")
plt.xlabel('Ángulo (rad)')
plt.ylabel('Valor')
plt.title('Seno y Coseno')
plt.legend()
plt.grid(True)
plt.show()