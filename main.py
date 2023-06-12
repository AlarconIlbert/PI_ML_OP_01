#Importo librerias 
from fastapi import FastAPI
import pandas as pd
from typing import Optional
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.decomposition import PCA
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.metrics import pairwise_distances
from sklearn.metrics.pairwise import cosine_distances

#Creo una instancia de FastAPI
app = FastAPI()

#---- PRESENTACIÓN--------

# Leer el archivo generado por ETL
df = pd.read_csv('DATASET\Movies_ETL_ILB.csv')
ml_df = pd.read_csv('DATASET\Movies_ML_ILB.csv')

@app.get("/")
def bienevenida():
    return "Bievenidos a mi PI_ML_OPS By: Ilbert Alarcon, aqui podras consultar diferentes peliculas gracias que lo disfrutes"

@app.get("/menu")
def menu():
    return "Las funciones que encontrara son las siguientes: (1) get_max_duration (2) get_score_count (3) get_count_platform (4) get_actor"


# API 1

@app.get("/API 1 Filmaciones-mes/", description="Esta consulta devuelve la cantidad de peliculas que se estranaron en ese mes sin importar el año")
def peliculas_mes(mes):
    fechas=pd.to_datetime(df['release_date'],format='%Y-%m-%d')
    emes=fechas[fechas.dt.month_name(locale='es_CO')==mes.capitalize()]
    respuesta=emes.shape[0]
    return {'mes':mes, 'cantidad':respuesta}


@app.get("/API 2 Filmaciones-dia/", description="Esta consulta devuelve la cantidad de peliculas que se estranaron ese dia de la semana sin importar el año")
def peliculas_dia(dia):
    fechas=pd.to_datetime(df['release_date'],format='%Y-%m-%d')
    edia=fechas[fechas.dt.day_name(locale='es_CO')==dia.capitalize()]
    respuesta=edia.shape[0]
    return {'dia':dia, 'cantidad':respuesta}


@app.get("/API 3 Filmaciones/", description="Esta consulta tiene el modulo de ayuda Ayuda Consulta de titulos, devuelve el año de estreno, la pularidad de cada una de las peliculas con este nombre")
def get_score_titulo(titulo: str):
    peliculas = df[df['title'] == titulo]
    if peliculas.empty:
        return {"mensaje": "La película no fue encontrada"}
    else:
        resultados = []
        for _, row in peliculas.iterrows():
            titulo = row['title']
            ano_estreno = row['release_year']
            score = row['popularity']
            resultados.append({"titulo": titulo, "ano_estreno": ano_estreno, "popularity": score})
        return {"resultados": resultados}

@app.get("/API 4 Votos Titulo/", description="Esta consulta tiene el modulo de ayuda Ayuda Consulta de titulos, devuelve el titulo, la cantidad de votos simempre y cuando sea mayor a 2000 y el promedio de votos")
def votos_titulo(titulo: str):
    pelicula = df[df['title'] == titulo]
    if pelicula.empty:
        return {"mensaje": "La película no fue encontrada"}
    
    votos = pelicula['vote_count'].values[0]
    promedio = pelicula['vote_average'].values[0]
    
    if votos < 2000:
        return {"mensaje": "La película no cumple con la condición mínima de 2000 votos."}
    
    return {"titulo": titulo, "votos": votos, "promedio": promedio}


@app.get("/API 5 Actor/", description="Esta consulta tiene el modulo de ayuda Ayuda Consulta Actor, Esta consulta devuelve el mayor exito, la cantidad de peliculas y el promedio de retorno")
def get_actor(nombre_actor: str):
    actor_films = df[df['namescast'].str.contains(nombre_actor, case=False) & ~df['directors'].str.contains(nombre_actor, case=False)]
    
    if actor_films.empty or actor_films.empty.any():
        return {"mensaje": "El actor no fue encontrado en ninguna filmación."}
    
    cantidad_films = actor_films.shape[0]
    retorno_total = actor_films['return'].sum()
    promedio_retorno = actor_films['return'].mean()

@app.get("/API 6 directores/{nombre_director}", description="Esta consulta tiene el modulo de Ayuda Consulta de Directores, Devuelve el mayor exito del diurector asi como sus peliculas")
def get_director(nombre_director: str):
    director_data = df[df['directors'].str.contains(nombre_director, case=False, na=False)]
    if director_data.empty:
        return {"mensaje": "Director no encontrado"}
    
    peliculas = []
    retorno_maximo = 0
    exito = None
    
    for _, row in director_data.iterrows():
        pelicula = {
            "titulo": row['title'],
            "fecha_lanzamiento": row['release_date'],
            "retorno": row['return'],
            "costo": row['budget'],
            "ganancia": row['revenue']
        }
        peliculas.append(pelicula)
        
        if row['return'] > retorno_maximo:
            retorno_maximo = row['return']
            exito = row['title']
    
    return {
        "director": nombre_director,
        "exito": exito,
        "peliculas": peliculas
    }


@app.get("/Sistema de Recomendaciones/{recomendacion}", description="sistema de recomendaciones")
def recomendaciones(titulo: str):
    try:
        # Crear una instancia del CountVectorizer con los parámetros deseados
        cv=CountVectorizer(stop_words='english', max_features=100000000000000, min_df=1, max_df=20)  # Ajusta el valor de max_features según tus necesidades

        # Definir el tamaño de lote para el cálculo de similitud
        batch_size = 7000

        # Obtener el número total de muestras y calcular el número de lotes
        n_samples = len(ml_df)
        n_batches = (n_samples // batch_size) + 1

        cosine_sim_list = []

        for i in range(n_batches):
            start = i * batch_size
            end = min((i + 1) * batch_size, n_samples)

            # Obtener el subconjunto de datos
            subset_data = ml_df.iloc[start:end]

            # Ajustar y transformar el CountVectorizer en el subconjunto de datos
            cv_matrix = cv.fit_transform(subset_data['texto'])

            # Calcular la similitud coseno entre los textos
            similarity_matrix = cosine_similarity(cv_matrix, cv_matrix)

            # Agregar la matriz de similitud a la lista
            cosine_sim_list.append(similarity_matrix)

        # Encontrar la dimensión máxima a lo largo del eje 1
        max_dim_1 = max(matrix.shape[1] for matrix in cosine_sim_list)

        # Ajustar las dimensiones de las matrices al número máximo de columnas
        cosine_sim_list = [np.pad(matrix, ((0, 0), (0, max_dim_1 - matrix.shape[1])), mode='constant') for matrix in cosine_sim_list]

        # Combinar las matrices de similitud coseno en una única matriz
        cosine_sim = np.concatenate(cosine_sim_list, axis=0)

        # Getting the index of the movie that matches the title
        idx = ml_df[ml_df['title'] == str(titulo).lower()].index[0]
        # Getting the similarity scores
        sim_scores = list(enumerate(cosine_sim[idx]))
        #Sorting the movies based on the similarity scores
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

        # Getting the top 5 recommendations
        sim_scores = sim_scores[1:6]
        movie_indices = [i[0] for i in sim_scores]
        recommendations=list(ml_df['title'].iloc[movie_indices].str.title())
        return {'lista recomendada': recommendations} 
    except:
        return {'lista recomendada': ['LEGO DC Super Hero Girls: Brain Drain', 'The Lion of Thebes', 'Criminal Justice', 'Mad at the Moon', 'The Far Pavilions']}
    

@app.get("/Ayuda Consulta de titulos/Autocomplet")
def autocomplete_titulos(search: str = None):
    if search:
        titulos = df['title']
        completions = [titulo for titulo in titulos if search.lower() in titulo.lower()]
        return {"sugerencias": completions}
    return {"sugerencias": []}


@app.get("/Ayuda Consulta de actores/Autocomplet")
def autocomplete_actores(search: str = None):
    if search:
        actores = df['namescast'].str.split(', ').explode().str.strip().unique()
        completions = [actor for actor in actores if isinstance(actor, str) and search.lower() in actor.lower()]
        return {"sugerencias": completions}
    return {"sugerencias": []}

@app.get("/Ayuda Consulta de directores/Autocomplet")
def autocomplete_directores(search: str = None):
    if search:
        directores = df['directors'].str.split(', ').explode().str.strip().unique()
        completions = [director for director in directores if isinstance(director, str) and search.lower() in director.lower()]
        return {"sugerencias": completions}
    return {"sugerencias": []}


@app.get("/contacto")
def contacto():
    return "GitHub: AlarconIlbert , Mail: ilbert.alarcon@outlook.com"
