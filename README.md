<center>

## **ETL (Extract - Transform - Load)**<br>
**_PROYECTO INDIVIDUAL 1_**<br>

</center>

**Machine Learning Operations (MLOps)**<br>
**Data Scientis:** _Ilbert Ferney Alarcon_ 😎<br>
**Cohorte 11**<br>


# PI_ML_OP_01

Repositorio PI-01 HENRY


# Sistema de Recomendaciones

## Descripción del proyecto

El Sistema de Recomendaciones es una aplicación que proporciona recomendaciones personalizadas de películas a los usuarios. Utiliza técnicas de filtrado colaborativo y contenido para calcular la similitud entre películas y generar recomendaciones basadas en los gustos y preferencias del usuario.

Este proyecto se ha desarrollado utilizando Python y diversas bibliotecas de machine learning y procesamiento de datos, como scikit-learn y pandas. Se ha implementado una API utilizando el framework FastAPI para permitir a los usuarios interactuar con el sistema de recomendaciones de forma sencilla y rápida.

## Características principales

- Generación de recomendaciones personalizadas basadas en el historial de películas del usuario.
- Soporte para filtrado colaborativo y contenido para mejorar la precisión de las recomendaciones.
- Interfaz de usuario intuitiva y fácil de usar mediante una API RESTful.
- Integración con una base de datos de películas para acceder a información detallada sobre cada película, como el título, género, reparto y director.

## Guía de instalación

Sigue estos pasos para instalar y ejecutar el Sistema de Recomendaciones en tu entorno local:

1. Clona este repositorio en tu máquina local.


git clone https://github.com/tu-usuario/sistema-recomendaciones.git

2. Ve al directorio del proyecto.

cd sistema-recomendaciones

3. Crea un entorno virtual e actívalo.

python -m venv env
source env/bin/activate

4. Instala las dependencias del proyecto.
pip install -r requirements.txt

5. Inicia la aplicación.
uvicorn main: app --reload


## Documentación de la API

La API proporciona varios endpoints para interactuar con el Sistema de Recomendaciones. A continuación se muestra una breve descripción de cada uno:

- `GET /recomendaciones/{usuario}`: Obtiene las recomendaciones personalizadas para un usuario específico.
- `POST /calificar/{usuario}/{pelicula}/{calificacion}`: Permite a un usuario calificar una película específica.
- `GET /peliculas/{genero}`: Obtiene una lista de películas filtradas por género.

Consulta la [documentación completa de la API](./docs/api-docs.md) para obtener más detalles sobre cada endpoint y cómo utilizarlos.

## Contribución

Si deseas contribuir al desarrollo del Sistema de Recomendaciones, sigue estos pasos:

1. Realiza un fork de este repositorio.
2. Crea una rama para tu contribución.
3. Realiza los cambios y mejoras en tu rama.
4. Envía un pull request describiendo tus cambios y el motivo de la contribución.

Agradecemos todas las contribuciones y sugerencias para mejorar este proyecto.

## Licencia

Este proyecto se distribuye bajo la licencia [MIT](./LICENSE).