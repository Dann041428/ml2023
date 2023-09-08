La app desarrollada con Python y la libreria Streamlit es una aplicacion web interactiva que nos permite desplegar modelos de aprendizaje supervisado (ML).

# API creado con Streamlit 
El editor de codigo fuente usado es Visual Studio Code, donde debemos 

    *   Instalar Python  

Para su correcto funcionamiento se requiere de las librerias 

    *   streamlit
    *   pandas
    *   numpy
    *   scikit-learn

Como agregamos imagenes en la app es necesario importar  
    *   pickle
    *   from PIL import Image


# Para su publicacion en Gcloud 

Producción en servidor remoto

    *   Activar una cuenta en google cloud
    *   Crear proyecto en google cloud
    *   Instalar GoogleCloudSDK
        (https://cloud.google.com/sdk/docs/install)
    *   Ejecutar en la terminal:
    
    $ gcloud init
    $ gcloud app deploy app.yaml --project "nombre del proyecto"

Es necesario contar con los archivos
    *   app.py
    *   .gcloudignore
    *   app.yaml 
    *   Dockerfile
    *   requirements.txt    
    *   "modelos a desplegar" (formato '.pkl')

    
