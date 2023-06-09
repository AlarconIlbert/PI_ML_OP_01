<p align="center">
<h2 align="center">PROYECTO INDIVIDUAL 1<br></h2>
</p>

<p align="center">
<a href="https://github.com/AlarconIlbert"><img src="https://img.shields.io/badge/python-FFFF0.svg?style=for-the-badge&logo=python&logoColor=0768a8&labelColor=ffffff" alt="python"></a> <img src="https://img.shields.io/badge/vscode-blue.svg?style=for-the-badge&logo=visual-studio-code&labelColor=ffffff&logoColor=blue" alt="vscode"> <a href="https://github.com/AlarconIlbert"><img src="https://img.shields.io/badge/github-black.svg?style=for-the-badge&logo=github&logoColor=black&labelColor=ffffff" alt="github"></a>
</p>

**Machine Learning Operations (MLOps)**<br>
**Data Scientis:** _Ilbert Ferney Alarcon_ 😎<br>

[![Linkedin: thaianebraga](https://img.shields.io/badge/-ILBERT-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/ilbert-ferney-alarcon-bothia/)](https://www.linkedin.com/in/anmol-p-singh/)![GitHub followers](https://img.shields.io/github/followers/AlarconIlbert?label=Follow&style=social) [![](https://img.shields.io/badge/Outlook-ilbert.alarcon@outlook.com-red)](mailto:ilbert.alarcon@outlook.com)

**Cohorte 11**<br>
**PI_ML_OP_01**<br>
Repositorio PI-01 HENRY

# Sistema de Recomendaciones

## Descripción del proyecto

El Sistema de Recomendaciones es una aplicación que proporciona recomendaciones personalizadas de películas a los usuarios. Utiliza técnicas de filtrado colaborativo y contenido para calcular la similitud entre películas y generar recomendaciones basadas en los gustos y preferencias del usuario.

Este proyecto se ha desarrollado utilizando Python y diversas bibliotecas de machine learning y procesamiento de datos, como scikit-learn y pandas. Se ha implementado una API utilizando el framework FastAPI para permitir a los usuarios interactuar con el sistema de recomendaciones de forma sencilla y rápida.

## Características principales

- Generación de recomendaciones personalizadas basadas en el historial de películas del usuario.
- Soporte para filtrado colaborativo y contenido para mejorar la precisión de las recomendaciones.
- Interfaz de usuario intuitiva y fácil de usar mediante FASTAPI.
- Integración con una base de datos de películas para acceder a información detallada sobre cada película, como el título, género, reparto y director.

## Guía de instalación

Sigue estos pasos para instalar y ejecutar el Sistema de Recomendaciones en tu entorno local:

1. Clona este repositorio en tu máquina local.


git clone https://github.com/AlarconIlbert/PI_ML_OP_01

2. Ve al directorio del proyecto.

```python
cd sistema-recomendaciones
```
3. Crea un entorno virtual e actívalo.
```python
python -m venv env
source env/bin/activate
```
4. Instala las dependencias del proyecto.
```python
pip install -r requirements.txt
```
5. Inicia la aplicación.
```python
uvicorn main:app --reload
```

## Documentación de la API

La API proporciona varios endpoints para interactuar con el Sistema de Recomendaciones. A continuación se muestra una breve descripción de cada uno:

- `GET /API 1 Filmaciones-mes/{mes}`: Esta consulta devuelve la cantidad de peliculas que se estranaron en ese mes sin importar el año.
- `GET /API 2 Filmaciones-dia/{dia}`: Esta consulta devuelve la cantidad de peliculas que se estranaron ese dia de la semana sin importar el año.
- `GET /API 3 Filmaciones/{titulo}`: Esta consulta tiene el modulo de ayuda Ayuda Consulta de titulos, devuelve el año de estreno, la pularidad de cada una de las peliculas con este nombre.
- `GET /API 4 Votos Titulo/{titulo}`: Esta consulta tiene el modulo de ayuda Ayuda Consulta de titulos, devuelve el titulo, la cantidad de votos simempre y cuando sea mayor a 2000 y el promedio de votos.
- `GET /API 5 Actor/{nombre_actor}`: Esta consulta tiene el modulo de ayuda Ayuda Consulta Actor, Esta consulta devuelve el mayor exito, la cantidad de peliculas y el promedio de retorno.
- `GET /API 6 directores/{nombre_director}`: Esta consulta tiene el modulo de Ayuda Consulta de Directores, Devuelve el mayor exito del diurector asi como sus peliculas.
- `GET /Sistema de Recomendaciones/{recomendacion}`: Esta consulta tiene el modulo de Ayuda Consulta de Titulos, Devuelve 5 recomendaciones de peliculas basadas en un analisis de contenido.


Consulta la [documentación completa](https://github.com/AlarconIlbert/PI_ML_OP_01/blob/master/requirements.txt) para obtener más detalles sobre cada endpoint y cómo utilizarlos.

## Deploy

https://fastapi-movies-pi-ilbert.onrender.com

## Contribución

Si deseas contribuir al desarrollo del Sistema de Recomendaciones, sigue estos pasos:

1. Realiza un fork de este repositorio.
2. Crea una rama para tu contribución.
3. Realiza los cambios y mejoras en tu rama.
4. Envía un pull request describiendo tus cambios y el motivo de la contribución.

Agradecemos todas las contribuciones y sugerencias para mejorar este proyecto.

## Licencia

Este proyecto se distribuye bajo la licencia [MIT](./LICENSE).

[![AlarconIlbert's github stats](https://github-readme-stats.vercel.app/api?username=AlarconIlbert&show_icons=true&theme=merko&hide=["contribs","issues"])](https://github.com/AlarconIlbert)