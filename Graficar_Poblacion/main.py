import read_csv
import graficas
import Utils


paises = read_csv.readCSV("Data.csv")

pais = input("escoge un pais para mostrar una grafica de su poblacion: ")
poblacion = Utils.obtener_poblacion_pais(paises,pais) # obtiene la poblacion para los años de abajo, para el pais seleccionado
# print(poblacion) #poblaciones del 2022 2020 2015 2010 2000 1990 1980 1970

graficas.graficar(poblacion,pais) # grafica un diabrama de 

continente_selesccionado = "South America" 
paises_seleccionados = list(filter(lambda continente : continente["Continent"] == continente_selesccionado,paises)) # filtra el total de paises a solo los del continente selesccionado

poblacion_mundial = Utils.poblacion_mundial(paises_seleccionados) # obtiene el dato de poblacion 2022 de cada pais que pase el filtro
# print(poblacion_mundial)
nombre_paises = list(poblacion_mundial.keys())
porcentaje_paises = list(poblacion_mundial.values())
graficas.graficoCircular(nombre_paises,porcentaje_paises) # crea grafica de torta con los paise filtrados

