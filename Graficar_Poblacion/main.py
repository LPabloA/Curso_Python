import os
os.system("cls")
# ------------
import read_csv
import graficas
import Utils


paises = read_csv.readCSV("App\Data.csv")
poblacion = Utils.obtener_poblacion(paises[8])
# print(poblacion) #poblaciones del 2022 2020 2015 2010 2000 1990 1980 1970
elementos = list(poblacion.keys())
# print(elementos)
valores = list(poblacion.values())
# print(valores)
# graficas.graficar(elementos, valores)

continente_selesccionado = "South America" 
paises_seleccionados = list(filter(lambda continente : continente["Continent"] == continente_selesccionado,paises)) # filtra el total de paises a solo los del continente selesccionado
poblacion_mundial = Utils.poblacion_mundial(paises_seleccionados)
print(poblacion_mundial)
nombre_paises = list(poblacion_mundial.keys())
porcentaje_paises = list(poblacion_mundial.values())
graficas.graficoCircular(nombre_paises,porcentaje_paises)

