import read_csv
import graficas
import Utils
import pandas as pd

# df = dataframes
df = pd.read_csv("Data.csv")
print(df[0:2])
df = df[df["Continent"] == "Asia"]
paises = df["Country/Territory"]
porcentajes = df["World Population Percentage"]
graficas.graficoCircular(paises,porcentajes)
