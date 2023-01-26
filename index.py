import pandas as pd
import uuid

amazon_df = pd.read_csv('./Datasets/amazon_prime_titles.csv', sep=',')
disney_df = pd.read_csv('./Datasets/disney_plus_titles.csv', sep=',')
hulu_df = pd.read_csv('./Datasets/hulu_titles.csv', sep=',')

# keys from every df
'''['show_id', 'type', 'title', 'director', 'cast', 'country', 'date_added', 'release_year', 'rating', 'duration', 'listed_in', 'description']'''

# Shapes
# amazon_df # 9668 x 12
# disney_df # 1450 x 12
# hulu_df # 3073 x 12
# 14_191
# Remplazar el str Entertainment, and Culture sin coma para que no tome como doble genero
amazon_df["listed_in"] = amazon_df["listed_in"].str.replace("Entertainment, and Culture", "Entertainment and Culture")
# Rellenamos nulos en la plataforma de hulu en la columna cast
hulu_df["cast"].fillna("Unknown actors", inplace=True)
amazon_df["duration"].fillna("Unknown Duration", inplace=True)


#1)
df_conc = pd.concat([amazon_df, disney_df, hulu_df])
#2)
df_conc["id"] = df_conc.apply(lambda _: uuid.uuid4(), axis=1)
#3)
df_conc["description"].fillna("No description", inplace=True)
df_conc["country"].fillna("No specified country", inplace=True)
df_conc["cast"].fillna("Unknown actors", inplace=True)

# print(df_conc.isna().sum())

#print(df_conc[df_conc["type"] == "TV Show"]["listed_in"].str.split(', ',expand=True).stack().value_counts())

#a)  Cantidad de veces que se repite un género y plataforma con mayor frecuencia del mismo. (Dificil)

# En la plataforma de Amazon cantidad de veces que se repite un género
''' print(amazon_df["listed_in"].str.split(', ',expand=True).stack().value_counts()) '''

# en la plataforma de Disney
''' print(disney_df["listed_in"].str.split(', ',expand=True).stack().value_counts()) '''

# en la plataforma de Hulu
''' print(hulu_df["listed_in"].str.split(', ',expand=True).stack().value_counts()) '''

# b) Actor que más se repite según plataforma y año. (Dificil)
# En la plataforma de Disney el actor que mas se repite
''' disney_df["cast"] = disney_df["cast"].str.split(", ")
res_df = disney_df.explode("cast")
grouped = res_df.groupby(["release_year"])
res = grouped["cast"].value_counts().sort_values().to_string()
print(res) '''
# En la plataforma de Amazon el actor que mas se repite
''' amazon_df["cast"] = amazon_df["cast"].str.split(", ")
res_df = amazon_df.explode("cast")
grouped = res_df.groupby(["release_year"])
res = grouped["cast"].value_counts().sort_values().to_string()
print(res) '''

# En la plataforma de Hulu el actor que mas se repite es un dato desconocido porque esta con nulos en toda la columna
''' res_df = hulu_df.explode("cast")
grouped = res_df.groupby(["release_year"])
res = grouped["cast"].value_counts().sort_values().to_string()
print(res) '''

# c)  Cantidad de películas y series (separado) por plataforma. (Medio)
'''
#En la plataforma de Amazon por TV Show (series):
print(amazon_df[amazon_df["type"] == "TV Show"].shape)
#y por Movie (peliculas)
print(amazon_df[amazon_df["type"] == "Movie"].shape)
#En la plataforma de Disneey por TV Show (series):
print(disney_df[disney_df["type"] == "TV Show"].shape)
#y por Movie (peliculas)
print(disney_df[disney_df["type"] == "Movie"].shape)
#En la plataforma de Hulu por TV Show (series):
print(hulu_df[hulu_df["type"] == "TV Show"].shape)
#y por Movie (peliculas)
print(hulu_df[hulu_df["type"] == "Movie"].shape) '''

# Cantidad de generos que se repiten basado en las peliculas
''' amazon_df[amazon_df["type"] == "Movie"]["listed_in"].str.split(', ', expand=True).stack().value_counts().to_string() ''' 

#d) Máxima duración según tipo de film (película/serie), por plataforma y por año (Medio)
grp = amazon_df[amazon_df["type"] == "Movie"].groupby(by=["release_year"], group_keys=True).apply(lambda x: x)
grp["duration"] = grp["duration"].str.extract("(\d+)").astype(int)
#^min$|.*\d+.*
#print(grp["duration"].max())
##################################################
##################################################
#print(grp.loc[grp.groupby("release_year")["duration"].idxmax()].reset_index())
#df.groupby("release_year")["duration"].max()


#print(grp.loc[grp['duration'].idxmax()])
#max_duration_row = grp.loc[grp['duration'].idxmax()]

#print(df_conc.groupby(["release_year"])[df_conc["type"] == "Movie"]["cast"].str.split(', ', expand=True).stack().value_counts())


#print(df_conc.loc[df_conc["type"] == "TV Show", ["release_year", "cast"]].value_counts())

#print(df_conc[df_conc["type"] == "TV Show"]["release_year"].value_counts())
# Get all words
#res = df_conc[df_conc['listed_in'].str.istitle()]

#e)  Peliculas que son exclusiva de una sola plataforma (hay que ingresar la plataforma ej. Netflix y debe retornar todas las peliculas que no aparezcan en las otras plataformas.
def get_movies_by_platform(platform):
  dicc = {
    "amazon": "amazon_prime_titles",
    "disney": "disney_plus_titles",
    "hulu": "hulu_titles"
  }
  # Creamos nuestro URL dinamico
  URL_FILE = "./Datasets/{df}.csv".format(df=dicc[platform])

  df = pd.read_csv(URL_FILE, sep=',')
  # Devolvemos las columnas que son peliculas (Movie)
  return df[df["type"] == "Movie"]
movies = get_movies_by_platform("amazon")
print(movies)

#f)  Autor o Autores que posean la mayor cantidad de peliculas filtrado por plataforma.
#50 Autores (directores) que posean mayor cantidad de peliculas en la plataforma de Amazon
''' print(amazon_df["director"].value_counts().head(50)) '''
#en la plataforma de Disney
''' print(disney_df["director"].value_counts().head(50)) '''
#en la plataforma de Hulu
''' print(hulu_df["director"].value_counts().head(50)) '''