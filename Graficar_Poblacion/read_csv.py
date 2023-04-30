import csv

def readCSV(elArchivo):
  with open(elArchivo,"r") as csvfile:
    reader = csv.reader(csvfile,delimiter=",")
    encabezado = next(reader) # imprime el encabezado del csv
    data = []
    for fila in reader:
      iterable = list(zip(encabezado,fila)) # une cada columna con su valor por dato en una lista de tuplas de (clumnna, valor)
      diccionario_paises = {titulo: valor for titulo, valor in iterable} # crea un diccionario donde cada clave queda asi: {clomuna: valor, ...}
      data.append(diccionario_paises) # agrega cada fila iterada a una lista
    return data


if __name__ == "__main__":
  data = readCSV("Data.csv")
  print(data[1:3]) # imprime el pais argentina (8)
  print(data[0]["Capital"]) # imprime la llave "capital del diccionario 0"