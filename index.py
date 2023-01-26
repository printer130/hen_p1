import pandas as pd
import uuid

df_1 = pd.read_csv('./Datasets/amazon_prime_titles.csv', sep=',')
df_2 = pd.read_csv('./Datasets/disney_plus_titles.csv', sep=',')
df_3 = pd.read_csv('./Datasets/hulu_titles.csv', sep=',')

# keys from every df
'''['show_id', 'type', 'title', 'director', 'cast', 'country', 'date_added', 'release_year', 'rating', 'duration', 'listed_in', 'description']'''

# Shapes
# df_1 # 9668 x 12
# df_2 # 1450 x 12
# df_3 # 3073 x 12
# 14_191
#1)
df_conc = pd.concat([df_1, df_2, df_3])
#2)
df_conc["id"] = df_conc.apply(lambda _: uuid.uuid4(), axis=1)
#3)
df_conc["description"].fillna("No description", inplace=True)
df_conc["country"].fillna("No specified country", inplace=True)
df_conc["cast"].fillna("Unknown actors", inplace=True)

# print(df_conc.isna().sum())

#print(df_conc[df_conc["type"] == "TV Show"]["listed_in"].str.split(', ',expand=True).stack().value_counts())

# a) Cantidad de veces que se repiten los generos por plataforma
# en la plataforma "TV Show"
'''
print(df_conc[df_conc["type"] == "TV Show"]["listed_in"].str.split(', ',expand=True).stack().value_counts())
'''
''' Drama            912
Comedy           727
Kids             603
Action           437
Animation        429
... '''

# en la plataforma "Movie"
'''
print(df_conc[df_conc["type"] == "Movie"]["listed_in"].str.split(', ',expand=True).stack().value_counts())
'''
''' Drama                    3816
Comedy                   2565
Action                   1775
Suspense                 1381 '''


# b) Actor que más se repite según plataforma y año. (Dificil)
''' df_conc["cast"] = df_conc["cast"].str.split(", ")
df_conc = df_conc.explode("cast")
grouped = df_conc.groupby(["type", "release_year"])
res = grouped["cast"].value_counts().sort_values().to_string()
print(res) '''

# c)  Cantidad de películas y series (separado) por plataforma. (Medio)
print(df_conc[df_conc["type"] == "Movie"])

#print(df_conc.groupby("release_year").count()[df_conc["type"] == "Movie"]["cast"].str.split(', ', expand=True).stack().value_counts())

# group by each year
#print(df_conc.groupby("release_year").())

#print(df_conc["cast"].value_counts())

#print(df_conc.loc[df_conc["type"] == "TV Show", ["release_year", "cast"]].value_counts())

#print(df_conc[df_conc["type"] == "TV Show"]["release_year"].value_counts())

# Get all words
#words_in_listed = list(df_conc['listed_in'].str.split(', ', expand=True).stack().unique())

# q = df_conc["listed_in"].str.split(', ',expand=True).stack().value_counts()

#print(df_conc.where(filter)["type"])
#print(df_conc.isnull().sum())
#print(df_conc.shape)
#print(df_conc.head())

#print(9668+1450+3073)
# print(count_nan)

# print(df["id"])

# listed in:type
# género   : plataforma

'''
a) Cantidad de veces que se repite un género y plataforma con mayor frecuencia del mismo. (Dificil)

b) Actor que más se repite según plataforma y año. (Dificil)

c) Cantidad de películas y series (separado) por plataforma. (Medio)

d) Máxima duración según tipo de film (película/serie), por plataforma y por año (Medio)

e) Peliculas que son exclusiva de una sola plataforma (hay que ingresar la plataforma ej. Netflix y debe retornar todas las peliculas que no aparezcan en las otras plataformas.

f) Autor o Autores que posean la mayor cantidad de peliculas filtrado por plataforma.
'''