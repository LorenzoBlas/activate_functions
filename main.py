import sys
import os
import matplotlib.pyplot as plt

def main():
    # Agregar el directorio que contiene srcs al path
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'srcs'))

    # Importar y ejecutar las funciones de activación
    from activation_functions.relu import plot_relu
    from activation_functions.sigmoid import plot_sigmoid
    from activation_functions.tanh import plot_tanh
    from activation_functions.leaky_relu import plot_leaky_relu

    funciones = [plot_relu, plot_sigmoid, plot_tanh, plot_leaky_relu]
    for func in funciones:
        try:
            func()
            plt.show()
        except Exception as e:
            print(f"Error al mostrar la gráfica: {e}")

if __name__ == "__main__":
    main()

