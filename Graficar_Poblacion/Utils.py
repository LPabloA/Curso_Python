
def obtener_poblacion(pais):
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
# if __name__ == "__main__":