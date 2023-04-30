import read_csv

def obtener_poblacion_pais(paises,pais_seleccion):
  pais = list(filter(lambda dicc: dicc["Country/Territory"] == pais_seleccion, paises))
  pais = pais[0]
  poblaciones  ={}
  for clave,valor in pais.items():
    if clave in list(pais.keys())[5:13]:
      poblaciones[clave] = int(valor)
  return poblaciones
  # hace lo mismo pero con (Comprehension)
  # poblaciones = {clave: valor for clave, valor in pais.items() if clave in list(pais.keys())[5:13]} 

def poblacion_mundial(data):
  poblacion_mundial = {}
  # pasa por cada pais del data
  for pais in data:
    valores_pais= list(pais.values())
    poblacion_mundial[valores_pais[2]] = float(valores_pais[16]) # agrega el nombre del pais como clave y el porcentaje como valor
  return poblacion_mundial
if __name__ == "__main__":
  paises = read_csv.readCSV("Data.csv")
  pais_seleccion = input("escoge un pais para mostrar una grafica de su poblacion: ")
  resultado = obtener_poblacion_pais(paises,pais_seleccion)
  print(resultado)
