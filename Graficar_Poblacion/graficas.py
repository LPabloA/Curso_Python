import matplotlib.pyplot as plt

def graficar(elementos,valores):
  fig,ax=plt.subplots() # fig = las cordenadas y ax = coordenadas
  ax.bar(elementos,valores) # dibuja un bar(diagrama de barras) con los valores y y los elementos
  plt.show()

def graficoCircular(elementos,valores):
  fig,ax=plt.subplots() # fig = las cordenadas y ax = coordenadas
  ax.pie(valores,labels=elementos) # dibuja un pie(grafico circular) con los valores y y los elementos (hay que especificar que los elemntos son los labels)
  ax.axis("equal") # para que la salida sea en la misma escala ciruclar
  plt.show() # muestra la figura

if __name__ == "__main__":
  graficar(["a","b","c"],[300.1,200,100])
  graficoCircular(["a","b","c"],[10,40,100])

# import numpy as np
# plt.figure()
# plt.plot(np.sin(np.linspace(-np.pi, np.pi, 1001)))
# plt.show()